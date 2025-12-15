import pygame as pg
import forms.controlador as con
import variablesyconst as var
import funciones as fun
import sys
from utn_fra.pygame_widgets import (
    Label, Button
)


def form_menu(datos_iniciales):
    menu_armado = {}

    screen = datos_iniciales["screen"] 
    menu_armado["screen"] = screen
    menu_armado["conf_musica"] = datos_iniciales.get("conf_musica")
    menu_armado["musica_path"] = var.FORMS_MUSICA["form_menu"]
    menu_armado["fondo"] = var.MENUE_SCALADO
    menu_armado["music_config"] = datos_iniciales.get('music_config')

    fuente_letra = pg.font.Font(var.FUENTELETRA, 30)
    ancho, alto = var.PANTALLA

    # --- TÍTULO ---
    menu_armado["lbl_titulo"] = Label(
        x=ancho // 2,
        y=80,
        text="EL DOGOR Z",
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=60,
        color=var.colores["naranja"],
        
    )

    # --- BOTONES ---
    espacio = 80

    
    menu_armado["btn_jugar"]= fun.crear_boton("JUGAR",fuente_letra, var.colores["blanco"],var.colores["azul"],
                                                ancho // 2 - 140, 200,w=280, h=50
                                    )
    
    menu_armado["btn_ranking"]= fun.crear_boton("RANKING",fuente_letra, var.colores["blanco"],var.colores["azul"],
                                                ancho // 2 - 140, 200 + espacio ,w=280, h=50
                                    )
    
    menu_armado["btn_opciones"]= fun.crear_boton("OPCIONES",fuente_letra, var.colores["blanco"],var.colores["azul"],
                                                ancho // 2 - 140 , 200 + 2*espacio ,w=280, h=50
                                    )
    menu_armado["btn_tutorial"] = fun.crear_boton(text="TUTORIAL",font=fuente_letra,txt_color=var.colores["blanco"],
                                                bg_color=var.colores["naranja"], x=var.PANTALLA[0] // 2 - 100,y=360,
                                                w=200, h=60
                                    )
    menu_armado["btn_salir"]= fun.crear_boton("SALIR",fuente_letra, var.colores["rojo"],var.colores["negro"],
                                                ancho // 2 - 140, 200 + 3*espacio ,w=280, h=50
                                    )
    
    menu_armado['widgets_list'] = [
        menu_armado.get('btn_jugar'),
        menu_armado.get('btn_ranking'),
        menu_armado.get('btn_opciones'),
        menu_armado.get("btn_tutorial"),
        menu_armado.get('btn_salir')
    ]
    
    return menu_armado


    
def dibujar_menu(form_menu):

    screen = pg.display.get_surface()
    

    screen.blit(var.MENUE_SCALADO, (0, 0))
    # Título
    form_menu["lbl_titulo"].draw()

    # Botones
    for boton in form_menu["widgets_list"]:
        fun.draw_button(screen, boton)


