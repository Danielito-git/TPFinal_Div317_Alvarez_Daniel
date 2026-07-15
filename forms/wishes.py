import pygame as pg
import variablesyconst as var
import funciones as fun
from utn_fra.pygame_widgets import Label


def form_wish_confirm(datos_iniciales):
    form_wish = {}
    form_wish['lugar'] = 'form_wish_confirm'
    form_wish['screen'] = datos_iniciales['screen']
    fuente_letra = pg.font.Font(var.FUENTELETRA, 25)

    form_wish['seleccion'] = Label(
        x=400,
        y=100,
        text='Selecciona tu deseo',
        screen=form_wish['screen'],
        font_path=var.FUENTELETRA,
        font_size=50,
        color=var.colores['blanco'],
    )

    form_wish['btn_heal_confirm'] = fun.crear_boton(
        text='HEAL',
        font=fuente_letra,
        txt_color=var.colores['blanco'],
        bg_color=var.colores['verde'],
        x=100,
        y=230,
        w=200,
        h=60,
    )

    form_wish['btn_shield_confirm'] = fun.crear_boton(
        text='SHIELD',
        font=fuente_letra,
        txt_color=var.colores['blanco'],
        bg_color=var.colores['azul'],
        x=475,
        y=230,
        w=200,
        h=60,
    )

    form_wish['btn_cancel'] = fun.crear_boton(
        text='CANCELAR',
        font=fuente_letra,
        txt_color=var.colores['blanco'],
        bg_color=var.colores['rojo'],
        x=290,
        y=320,
        w=200,
        h=60,
    )

    form_wish['lista_botones'] = [
        form_wish['btn_heal_confirm'],
        form_wish['btn_shield_confirm'],
        form_wish['btn_cancel'],
    ]

    return form_wish


def dibujar_wish_confirm(form_wish):
    screen = form_wish['screen']
    screen.blit(var.WISH_ESCALADO, (0, 0))
    form_wish['seleccion'].draw()

    for boton in form_wish['lista_botones']:
        fun.draw_button(screen, boton)


def redirigir_form_wish(form_juego, datos_iniciales, eve):
    boton_heal = form_juego.get("btn_heal")

    if boton_heal["rect"].collidepoint(eve.pos):
        datos_iniciales["lugar"] = "form_wish_confirm"


def manejo_evento_wish(datos_iniciales, form_wishes, eventos):
    usados = datos_iniciales.setdefault("wishes_usados", {"heal": False, "shield": False})

    for ev in eventos:
        if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:

            if form_wishes["btn_heal_confirm"]["rect"].collidepoint(ev.pos):
                
                if not usados["heal"]:
                    datos_iniciales["wishes"]["heal"] = True
                    usados["heal"] = True
                datos_iniciales["lugar"] = "form_jugar"

            elif form_wishes["btn_shield_confirm"]["rect"].collidepoint(ev.pos):

                if not usados["shield"]:
                    datos_iniciales["wishes"]["shield"] = True
                    datos_iniciales["shield_activo"] = True
                    usados["shield"] = True
                datos_iniciales["lugar"] = "form_jugar"


            elif form_wishes["btn_cancel"]["rect"].collidepoint(ev.pos):
                datos_iniciales["lugar"] = "form_jugar"


def actualizar_wish_confirm(datos_iniciales, eventos=None):
    form_wishes = form_wish_confirm(datos_iniciales)
    dibujar_wish_confirm(form_wishes)
    
    if eventos:
        manejo_evento_wish(datos_iniciales, form_wishes, eventos)
