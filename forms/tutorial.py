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

    ancho, alto = var.PANTALLA
    fuente_normal = pg.font.Font(var.FUENTELETRA, 28)
    fuente_tutos = 25

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

    tutorial["imagenes_descripciones"] = {
        0: "Este boton nos hace jugar la mano de nuestro mazo",
        1: "El boton heal te cura un porcentaje de tu vida en una tirada",
        2: "El boton shield te protege de una derrota y refleja el dano",
        3: "Aqui se comparan tu cartas con las del rival\nla carta que tenga mas ATK gana la mano",
        4: "Te pedira tu nombre y lo guardara en el archivo csv",
        5: "Tu cantidad de puntos conseguidos",
        6: "El tiempo que tendras para jugar la partida",
        7: "El ranking de los mejores jugadores y sus puntajes",
    }

    tutorial["lbl_descripcion"] = Label(
        x=ancho // 2,
        y=100,
        text="",
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=fuente_tutos,
        color=var.colores.get("blanco", pg.Color("white")),
    )

    tutorial["indice_actual_img"] = 0

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
    

    btn_w, btn_h = 160, 48
    

    tutorial["btn_previo"] = fun.crear_boton(
        "PREVIO", fuente_normal, var.colores.get("blanco"), var.colores.get("naranja"),
        120, 470, w=btn_w, h=btn_h
    )

    tutorial["btn_volver"] = fun.crear_boton(
        "VOLVER", fuente_normal, var.colores.get("rojo"), var.colores.get("naranja"),
        360, 550, w=btn_w, h=btn_h
    )

    tutorial["btn_siguiente"] = fun.crear_boton(
        "SIGUIENTE", fuente_normal, var.colores.get("blanco"), var.colores.get("naranja"),
        550, 470, w=btn_w, h=btn_h
    )

    tutorial["widgets_list"] = [
        tutorial["btn_previo"],
        tutorial["btn_volver"],
        tutorial["btn_siguiente"],
    ]

    return tutorial

def ajustar_indice_recursivo(indice: int, cambio: int, longitud: int) -> int:
    if longitud <= 0:
        return 0
    if cambio == 0:
        return indice % longitud

    if cambio > 0:
        siguiente = indice + 1
        if siguiente >= longitud:
            siguiente = 0
        return ajustar_indice_recursivo(siguiente, cambio - 1, longitud)

    anterior = indice - 1
    if anterior < 0:
        anterior = longitud - 1
    return ajustar_indice_recursivo(anterior, cambio + 1, longitud)


def avanzar_tutorial(form: dict, direccion: int):
    form["indice_actual_img"] = ajustar_indice_recursivo(
        form["indice_actual_img"], direccion, len(form["imagenes"])
    )


def dibujar_tutorial(form_tutorial: dict):
    screen = form_tutorial["screen"]

    screen.blit(var.TUTO_ESCALADO, (0, 0))

    form_tutorial["lbl_titulo"].draw()

    indice_img = form_tutorial["indice_actual_img"]
    imagen_actual = form_tutorial["imagenes"][indice_img]
    descripcion = form_tutorial["imagenes_descripciones"].get(indice_img, "")
    
    form_tutorial["lbl_descripcion"].update_text(descripcion, pg.Color('white'))

    screen.blit(imagen_actual, (300, 270))
    form_tutorial["lbl_descripcion"].draw()

    for boton in form_tutorial["widgets_list"]:
        fun.draw_button(screen, boton)


def actualizar_tutorial(datos_iniciales, eventos=None):
    if "form_tutorial" not in datos_iniciales:
        datos_iniciales["form_tutorial"] = form_tutorial(datos_iniciales)

    form = datos_iniciales["form_tutorial"]
    dibujar_tutorial(form)

    if eventos:
        for ev in eventos:
            if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:
                if form["btn_siguiente"]["rect"].collidepoint(ev.pos):
                    avanzar_tutorial(form, 1)
                elif form["btn_previo"]["rect"].collidepoint(ev.pos):
                    avanzar_tutorial(form, -1)
                elif form["btn_volver"]["rect"].collidepoint(ev.pos):
                    datos_iniciales["lugar"] = "form_menu"
