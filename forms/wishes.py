import pygame as pg
import variablesyconst as var
import funciones as fun
from utn_fra.pygame_widgets import Label

def form_wish_confirm(datos_iniciales):
    form_wish = {}

    form_wish["lugar"] = "form_wish_confirm"
    form_wish["screen"] = datos_iniciales["screen"]
    fuente_letra = pg.font.Font(var.FUENTELETRA, 25)

    form_wish["seleccion"] = Label(x=400, y=100, text="Selecciona tu deseo",
                                screen=form_wish.get("screen"), font_path=var.FUENTELETRA,
                                font_size=50, color=var.colores["blanco"]

    )

    form_wish["btn_heal_confirm"] = fun.crear_boton(
        text="HEAL",
        font=fuente_letra,
        txt_color=var.colores["blanco"],
        bg_color=var.colores["verde"],
        x=100, y=230, w=200, h=60
    )

    form_wish["btn_shield_confirm"] = fun.crear_boton(
        text="SHIELD",
        font=fuente_letra,
        txt_color=var.colores["blanco"],
        bg_color=var.colores["azul"],
        x=475, y=230, w=200, h=60
    )

    form_wish["btn_cancel"] = fun.crear_boton(
        text="CANCELAR",
        font=fuente_letra,
        txt_color=var.colores["blanco"],
        bg_color=var.colores["rojo"],
        x=290, y=320, w=200, h=60
    )

    form_wish["lista_botones"] = [
        form_wish["btn_heal_confirm"],
        form_wish["btn_shield_confirm"],
        form_wish["btn_cancel"]
    ]

    return form_wish

def manejo_evento_wish(datos_iniciales,form_wishes, eventos):
    for ev in eventos:
        if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:

            if form_wishes["btn_heal_confirm"]["rect"].collidepoint(ev.pos):
                datos_iniciales["wishes"]["heal"] = True
                print("WISH HEAL ACTIVADO")
                datos_iniciales["lugar"] = "form_jugar"

            elif form_wishes["btn_shield_confirm"]["rect"].collidepoint(ev.pos):
                datos_iniciales["wishes"]["shield"] = True
                datos_iniciales["shield_activo"] = True
                print("WISH SHIELD ACTIVADO")
                datos_iniciales["lugar"] = "form_jugar"

            elif form_wishes["btn_cancel"]["rect"].collidepoint(ev.pos):
                print("WISH CANCELADO")
                datos_iniciales["lugar"] = "form_jugar"

def redirigir_form_wish(form_juego, datos_iniciales, eve):
    boton_heal = form_juego.get("btn_heal")
    if boton_heal["rect"].collidepoint(eve.pos):
        datos_iniciales["lugar"] = "form_wish_confirm"

def ejecutar_wish(datos):
    wishes = datos["wishes"]

    if wishes["heal"]:
        datos["vida_jugador"] += datos["vida_max_jugador"]
        wishes["heal"] = False  # 🔥 consumir wish

    # SHIELD
    if wishes["shield"]:
        datos["shield_activo"] = True
        wishes["shield"] = False

    return datos

# def verificar_wish(perdedor, datos, form_juego, damage):
#     if perdedor == "jugador":
#             if datos.get("shield_activo"):
#                 form_juego["vida_enemigo"] -= damage
#                 datos["shield_activo"] = False
#             else:
#                 form_juego["vida_jugador"] -= damage

#     elif perdedor == "enemigo":
#             form_juego["vida_enemigo"] -= damage


def dibujar_wish_confirm(form_wish):
    screen = form_wish["screen"]
    screen.blit(var.WISH_ESCALADO, (0, 0))

    form_wish.get("seleccion").draw()

    for boton in form_wish["lista_botones"]:
        fun.draw_button(screen, boton)