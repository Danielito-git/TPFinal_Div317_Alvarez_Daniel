import pygame as pg
import variablesyconst as var
import funciones as fun
from utn_fra.pygame_widgets import Label


def form_tutorial(datos_iniciales):
    """
    Crea y devuelve el diccionario del form 'form_tutorial'.
    Mantiene el estilo y claves similares a form_opciones.py para integrarse con el controlador.
    """
    tutorial = {}
    screen = datos_iniciales["screen"]
    tutorial["screen"] = screen
    tutorial["lugar"] = "form_tutorial"
    tutorial["conf_musica"] = datos_iniciales.get("conf_musica")
    #tutorial["musica_path"] = var.FORMS_MUSICA.get("form_tutorial") if hasattr(var, "FORMS_MUSICA") else None

    ancho, alto = var.PANTALLA
    fuente_normal = pg.font.Font(var.FUENTELETRA, 28)
    fuente_titulo = pg.font.Font(var.FUENTELETRA, 48)

    tutorial["imagenes"] = [
        var.imagen_tuto_1,
        var.imagen_tuto_2,
        var.imagen_tuto_3,
        var.imagen_tuto_4,
        var.imagen_tuto_5,
        var.imagen_tuto_6,
        var.imagen_tuto_7,
        var.imagen_tuto_8
    ]

    tutorial["indice_actual"] = 0

    # Título
    tutorial["lbl_titulo"] = Label(
        x=ancho // 2,
        y=60,
        text="Tutorial",
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=48,
        color=var.colores.get("blanco", pg.Color("white")),
    )
    
    tutorial["lbl_descripcion"] = Label(
        x=ancho // 2,
        y=alto - 120,
        text="",  
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=26,
        color=pg.Color("white"),
    )

    btn_w, btn_h = 160, 48
    y = alto - btn_h - 20
    espacio = 20
    x_center = ancho // 2

    tutorial["btn_previo"] = fun.crear_boton(
        "PREVIO", fuente_normal, var.colores.get("blanco"), var.colores.get("naranja"),
        x_center - btn_w - espacio, y, w=btn_w, h=btn_h
    )

    tutorial["btn_volver"] = fun.crear_boton(
        "VOLVER", fuente_normal, var.colores.get("rojo"), var.colores.get("naranja"),
        x_center - btn_w//2, y, w=btn_w, h=btn_h
    )

    tutorial["btn_siguiente"] = fun.crear_boton(
        "SIGUIENTE", fuente_normal, var.colores.get("blanco"), var.colores.get("naranja"),
        x_center + espacio + 0, y, w=btn_w, h=btn_h
    )

    tutorial["widgets_list"] = [
        tutorial["btn_previo"],
        tutorial["btn_volver"],
        tutorial["btn_siguiente"],
    ]

    return tutorial

def avanzar_tutorial(form: dict):
    form["indice_actual"] += 1

    if form["indice_actual"] >= len(form["imagenes"]):
        form["indice_actual"] = 0

def retroceder_tutorial(form: dict):
    form["indice_actual"] -= 1

    if form["indice_actual"] < 0:
        form["indice_actual"] = len(form["imagenes"]) - 1

def dibujar_tutorial(form_tutorial: dict):
    screen = form_tutorial["screen"]

    screen.blit(var.TUTO_ESCALADO, (0, 0))

    form_tutorial["lbl_titulo"].draw()
    form_tutorial["lbl_indicador"].draw()
    form_tutorial["lbl_descripcion"].draw()

    for boton in form_tutorial["widgets_list"]:
        fun.draw_button(screen, boton)
