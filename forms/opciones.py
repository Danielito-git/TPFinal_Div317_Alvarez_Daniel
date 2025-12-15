import pygame as pg
import forms.controlador as con
import confsonido as sonido
import funciones as fun
import variablesyconst as var
import sys
from utn_fra.pygame_widgets import (
    Label
)


def form_opciones(datos_iniciales):
    opciones_armado = {}

    screen = datos_iniciales["screen"] 
    opciones_armado["screen"] = screen 
    opciones_armado["lugar"] = "form_opciones"
    opciones_armado["conf_musica"] = datos_iniciales.get("conf_musica")
    opciones_armado["musica_path"] = var.FORMS_MUSICA["form_opciones"]
    opciones_armado["conf_musica"] = datos_iniciales.get('conf_musica')
    fuente_letra = pg.font.Font(var.FUENTELETRA, 30)
    ancho, alto = var.PANTALLA

   
    opciones_armado["lbl_titulo"] = Label(
        x=ancho // 2,
        y=80,
        text="Opciones",
        screen=opciones_armado.get("screen"),
        font_path=var.FUENTELETRA,
        font_size=60,
        color=var.colores["blanco"],
        
    )

    
    espacio = 110
    
    opciones_armado["btn_musica"]= fun.crear_boton("Musica",fuente_letra, var.colores["blanco"],var.colores["naranja"],
                                                ancho // 2 - 140,130,w=280, h=50
                                    )
    
    opciones_armado["btn_mas"]= fun.crear_boton("+",fuente_letra,var.colores["blanco"],var.colores["naranja"],
                                                ancho // 2 + espacio, 280,w=60, h=60
                                    )
    
    opciones_armado["btn_menos"]= fun.crear_boton("-",fuente_letra,var.colores["blanco"],var.colores["naranja"],
                                                ancho // 2 - espacio - 60,280,w=60, h=60,
                                    )
    
    opciones_armado["lbl_volumen"]=  Label(ancho // 2, y=310,text=f'{sonido.get_actual_volume()}', screen=screen,
                                    font_path=var.FUENTELETRA, font_size=55, color=pg.Color('white'))
    
    opciones_armado["btn_volver"]= fun.crear_boton("Volver", fuente_letra, var.colores["rojo"], var.colores["naranja"],
                                                ancho // 2 - 100,450, 200, 50
                                    )

    opciones_armado['widgets_list'] = [
        opciones_armado.get('btn_musica'),
        opciones_armado.get("btn_mas"),
        opciones_armado.get("btn_menos"),
        opciones_armado.get("btn_volver")
    ]
    return opciones_armado



def dibujar_opciones(form_opciones, form_controlador):

    screen = pg.display.get_surface()
    screen.blit(var.OPCIONES_ESCALADO, (0, 0))
    volumen = int(form_controlador["conf_musica"]["volumen"])
    form_opciones["lbl_volumen"].texto = f"{volumen}%"
    
    # botones
    for boton in form_opciones["widgets_list"]:
        fun.draw_button(screen, boton)

    # titulos
    form_opciones["lbl_titulo"].draw()
    form_opciones["lbl_volumen"].draw()


def volver_menu(form_controlador, form_opciones, evento):
    if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
        mx, my = evento.pos

        # Si hizo clic en el botón VOLVER
        if form_opciones["btn_volver"]["rect"].collidepoint(mx, my):
            form_controlador["lugar"] = "form_menu"
    
    