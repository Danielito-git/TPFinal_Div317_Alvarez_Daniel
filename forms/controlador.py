import pygame as pg
import forms.menu as menu
import forms.opciones as op
import variablesyconst as var
import funciones as fun
import forms.juego as juego
import forms.final as fin
import forms.ranking as ranking
import forms.tutorial as tuto
import confsonido as sonido
import forms.wishes as wi
import sys

def cambiar_lugar(datos_iniciales: dict, form_menu:dict, mouse_pos):
    
    for boton in form_menu["widgets_list"]:
         if boton["rect"].collidepoint(mouse_pos):
           
            match boton["text"]:
                case "JUGAR":
                    datos_iniciales["lugar"] = "form_jugar"

                case "RANKING":
                    datos_iniciales["lugar"] = "form_ranking"

                case "OPCIONES":
                    datos_iniciales["lugar"] = "form_opciones"

                case "SALIR":
                    print("SALIENDING")
                    pg.quit()
                    sys.exit()
    return datos_iniciales


def update_forms(datos_iniciales: dict, eventos=None):
    sonido.reproducir_musica_lugar(datos_iniciales)
    lugar = datos_iniciales.get("lugar")
    

    match lugar:
        case "form_menu":
            form_menu = menu.form_menu(datos_iniciales)
            menu.dibujar_menu(form_menu)
            if eventos:
                for eve in eventos:
                    if eve.type == pg.MOUSEBUTTONDOWN and eve.button == 1:
                        cambiar_lugar(datos_iniciales, form_menu, eve.pos)
        case "form_jugar":

            if "form_juego" not in datos_iniciales:
                datos_iniciales["form_juego"] = juego.form_juego(datos_iniciales)
            
            if datos_iniciales.get("juego_terminado"):
                return
            form_juego = datos_iniciales["form_juego"]
            juego.dibujar_juego(form_juego, datos_iniciales)
            
            if eventos:
                for eve in eventos:
                    if eve.type == pg.MOUSEBUTTONDOWN and eve.button == 1:
                        boton_play = form_juego["btn_play"]
                        if boton_play["rect"].collidepoint(eve.pos):
                            
                            datos_iniciales["jugar_pendiente"] = True
                        wi.redirigir_form_wish(form_juego, datos_iniciales, eve)


            if datos_iniciales.get("jugar_pendiente"):
                print("WISHES:", datos_iniciales["wishes"])
                juego.ejecutar_jugada(form_juego, datos_iniciales)
                datos_iniciales["jugar_pendiente"] = False
                
            #print("estoy jugando wiiiiiiii")

        case "form_ranking":
            form_ranking = ranking.form_ranking(datos_iniciales)
            ranking.dibujar_ranking(form_ranking)
            for evento in eventos:
                ranking.volver_menu(datos_iniciales, form_ranking, evento)
            

        case "form_opciones":
            form_opciones = op.form_opciones(datos_iniciales)
            op.dibujar_opciones(form_opciones, datos_iniciales)
                
            for evento in eventos:
                sonido.evento_mute_desmute(datos_iniciales, form_opciones, evento)
                sonido.subir_bajar_vol(form_opciones, evento)
                op.volver_menu(datos_iniciales, form_opciones, evento)
        case "form_game_over":
            if "form_game_over" not in datos_iniciales:
                datos_iniciales["form_game_over"] = fin.form_juego_terminado(datos_iniciales)

            form_final = datos_iniciales["form_game_over"]
            fin.dibujar_game_over(form_final, datos_iniciales)
            for eve in eventos:
                if eve.type == pg.KEYDOWN and form_final["activo"]:
                    if eve.key == pg.K_BACKSPACE:
                        form_final["player"] = form_final["player"][:-1]
                    elif eve.key == pg.K_RETURN:
                        fin.guardar_puntos(form_final["player"], datos_iniciales)
                        fun.resetear_estado_juego(datos_iniciales)
                        datos_iniciales["lugar"] = "form_menu"
                    else:
                        form_final["player"] += eve.unicode
        case "form_wish_confirm":
            if "form_wish_confirm" not in datos_iniciales:
                datos_iniciales["form_wish_confirm"] = wi.form_wish_confirm(datos_iniciales)

            form_wishes = datos_iniciales["form_wish_confirm"]
            wi.dibujar_wish_confirm(form_wishes)
            
            if eventos:
                wi.manejo_evento_wish(
                    datos_iniciales,
                    form_wishes,
                    eventos
                )
        case "form_tutorial":
            if "form_tutorial" not in datos_iniciales:
                datos_iniciales["form_tutorial"] = tuto.form_tutorial(datos_iniciales)

            form = datos_iniciales["form_tutorial"]
            tuto.dibujar_tutorial(form)

            if eventos:
                for ev in eventos:
                    if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:

                        if form["btn_siguiente"]["rect"].collidepoint(ev.pos):
                            tuto.avanzar_tutorial(form)

                        elif form["btn_previo"]["rect"].collidepoint(ev.pos):
                            tuto.retroceder_tutorial(form)

                        elif form["btn_volver"]["rect"].collidepoint(ev.pos):
                            datos_iniciales["lugar"] = "form_menu"
            

                