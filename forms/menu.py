import pygame as pg
import variablesyconst as var
import funciones as fun
import forms.controlador as controlador
from utn_fra.pygame_widgets import Label


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

    menu_armado["lbl_titulo"] = Label(
        x=ancho // 2,
        y=80,
        text="EL DOGOR Z",
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=60,
        color=var.colores["naranja"],
        
    )

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
                                                bg_color=var.colores["naranja"], x=570,y=500,
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
    form_menu["lbl_titulo"].draw()

    for boton in form_menu["widgets_list"]:
        fun.draw_button(screen, boton)


def actualizar_menu(datos_iniciales, eventos=None):
    form_menu_data = form_menu(datos_iniciales)
    dibujar_menu(form_menu_data)

    if eventos:
        for eve in eventos:
            if eve.type == pg.MOUSEBUTTONDOWN and eve.button == 1:
                controlador.cambiar_lugar(datos_iniciales, form_menu_data, eve.pos)


