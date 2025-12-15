import pygame as pg
import funciones as fun
import variablesyconst as var
import os
import csv
from utn_fra.pygame_widgets import Label

def form_juego_terminado(datos_iniciales):
    form_final = {}

    screen = datos_iniciales["screen"]
    form_final["activo"] = True
    form_final["tema_actual"] = var.FORMS_MUSICA["form_final_victoria"]
    form_final["screen"] = screen
    form_final["player"] = ""
    form_final["conf_musica"] = datos_iniciales.get("conf_musica")
    form_final["lugar"] = "form_game_over"

    fuente_letra = pg.font.Font(var.FUENTELETRA, 30)

    form_final["titulo"] = Label( x=var.PANTALLA[0] // 2, y=95,text="FIN DEL JUEGO",screen=screen,
                                font_path=var.FUENTELETRA,font_size=50,color=var.colores["blanco"],
        )


    # input simple

    form_final["btn_guardar"] = fun.crear_boton("Guardar",fuente_letra, var.colores["blanco"],var.colores["azul"],
                                                var.PANTALLA[0] // 2 - 140, 280 ,w=280, h=50)

    return form_final


def guardar_puntos(nombre, datos):
    archivo = "puntajes.csv"
    existe = os.path.exists(archivo)

    with open(archivo, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not existe:
            writer.writerow(["nombre", "puntos"])

        writer.writerow([
            nombre,
            datos.get("puntos_totales")
        ])



def dibujar_game_over(form_final, datos_iniciales):
    screen = form_final["screen"]
    ganador = datos_iniciales.get("ganador")
    
    if ganador == "jugador":
        screen.blit(var.VICTORIA_ESCALADA, (0,0))
    else:
        screen.blit(var.DERROTA_ESCALADA, (0,0))

    form_final.get("titulo").draw()

    font = pg.font.Font(None, 40)
    txt = font.render(f"Nombre: {form_final['player']}", True, (255,255,255), (0, 0, 0))
    screen.blit(txt, (250, 200))
    

    fun.draw_button(screen, form_final["btn_guardar"])

