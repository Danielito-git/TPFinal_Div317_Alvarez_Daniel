import pygame as pg
import confsonido as sonido
import variablesyconst as var
import forms.controlador as con
import sys


def iniciar_juego():
    
    pg.init()
    pg.mixer.init()

    pamtalla = pg.display.set_mode(var.PANTALLA)
    pg.display.set_caption("Mi jueguito lindo")
    

    corriendo = True
    reloj = pg.time.Clock()
    datos_juego = {
        "puntos_totales" : 0,
        "player": "",
        "intentos" : var.VIDASTOTALES,
        "screen": pamtalla,
        "lugar": "form_menu",
        "tema_actual": var.FORMS_MUSICA["form_menu"],
        "tiempo_restante_ms": var.TIMER_JUEGO * 1000,
        "ultimo_tick_ms": pg.time.get_ticks(),
        "juego_terminado" : False,
        "ganador": None,
        "carta_jugador_actual": None,
        "carta_enemigo_actual": None,
        "conf_musica": {
           "volumen" : var.VOLUMEN,
           "apagada" : False,
           "prendida" : True
        }
    }
    datos_juego["wishes"] = {
        "heal": False,
        "shield": False
    }
    datos_juego["shield_activo"] = False

    sonido.iniciar_musica(datos_juego["conf_musica"]["volumen"],datos_juego["tema_actual"])

    while corriendo == True:

        eventos = pg.event.get()

        for evento in eventos:
            if evento.type == pg.QUIT:
                corriendo = False

        
        con.update_forms(datos_juego, eventos)
        sonido.reproducir_musica_lugar(datos_juego)

        pg.display.set_icon(var.ICONOJUEGO)
        pg.display.flip()
        
        reloj.tick(30)
    
    pg.quit()
    sys.exit()
