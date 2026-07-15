import pygame as pg
import menu as menu
import opciones as op
import juego as juego
import final as fin
import ranking as ranking
import tutorial as tuto
import wishes as wish
import confsonido as sonido
import variablesyconst as var
import funciones as fun
import sys

def cambiar_lugar(datos_iniciales: dict, form_menu: dict, mouse_pos):
    for boton in form_menu["widgets_list"]:
        if boton["rect"].collidepoint(mouse_pos):
            match boton["text"]:
                case "JUGAR":
                    datos_iniciales["lugar"] = "form_jugar"
                case "RANKING":
                    datos_iniciales["lugar"] = "form_ranking"
                case "OPCIONES":
                    datos_iniciales["lugar"] = "form_opciones"
                case "TUTORIAL":
                    datos_iniciales["lugar"] = "form_tutorial"
                case "SALIR":
                    print("SALIENDING")
                    pg.quit()
                    sys.exit()
    return datos_iniciales


def update_forms(datos_iniciales: dict, eventos=None):
    if datos_iniciales.get("salir"):
        pg.quit()
        sys.exit()

    sonido.reproducir_musica_lugar(datos_iniciales)
    lugar = datos_iniciales.get("lugar")

    match lugar:
        case "form_menu":
            menu.actualizar_menu(datos_iniciales, eventos)
        case "form_jugar":
            juego.actualizar_juego(datos_iniciales, eventos)
        case "form_ranking":
            ranking.actualizar_ranking(datos_iniciales, eventos)
        case "form_opciones":
            op.actualizar_opciones(datos_iniciales, eventos)
        case "form_game_over":
            if "form_game_over" not in datos_iniciales:
                datos_iniciales["form_game_over"] = fin.form_juego_terminado(datos_iniciales)

            form_final = datos_iniciales["form_game_over"]
            fin.actualizar_game_over(form_final, datos_iniciales, eventos)
        case "form_wish_confirm":
            wish.actualizar_wish_confirm(datos_iniciales, eventos)
        case "form_tutorial":
            tuto.actualizar_tutorial(datos_iniciales, eventos)
