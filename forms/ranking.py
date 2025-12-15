import pygame as pg
import forms.controlador as con
import confsonido as sonido
import variablesyconst as var
import funciones as fun
import sys
import csv
import os
from utn_fra.pygame_widgets import Label


def form_ranking(datos_iniciales):
    ranking_armado = {}

    screen = datos_iniciales["screen"] 
    ranking_armado["screen"] = screen 
    ranking_armado["lugar"] = "form_ranking"
    ranking_armado["conf_musica"] = datos_iniciales.get("conf_musica")
    
    
    ranking_armado["musica_path"] = var.FORMS_MUSICA["form_ranking"],
    ranking_armado["fondo"] = var.MENUE_SCALADO
    ranking_armado["conf_musica"] = datos_iniciales.get('conf_musica')
    
    fuente_letra = pg.font.Font(var.FUENTELETRA, 30)
    ancho, alto = var.PANTALLA

    top10 = obtener_tops("puntajes.csv")

    ranking_armado["lista_top10"] = top10
    ranking_armado["labels_top10"] = []
    
    labels = []
    y_base = 220

    for i in range(10):
        nombre, puntaje = top10[i]
        y = y_base + (i * 25)

        lbl = Label(
            x=ancho // 2,
            y=y,
            text=f"{i+1}.   {nombre}    {puntaje}",
            screen=screen,
            font_path=var.FUENTELETRA,
            font_size=27,
            color=var.colores["blanco"],
        )
        labels.append(lbl)

    ranking_armado["labels_top10"] = labels
    
    ranking_armado["lbl_titulo"] = Label(
        x=ancho // 2,
        y=90,
        text="Ranking jugadores",
        screen=ranking_armado.get("screen"),
        font_path=var.FUENTE_NUMERO,
        font_size=50,
        color=var.colores["blanco"],
    )
    

    ranking_armado["lbl_subtitulo"] = Label(x=ancho // 2, y=150, text="TOP 10 jugadores", screen=screen, font_path=var.FUENTELETRA,
        font_size=30, color=var.colores["blanco"])
    
    ranking_armado['btn_volver'] = fun.crear_boton("Volver", fuente_letra, var.colores["blanco"], var.colores["negro"],
                                                ancho // 2 - 100, 485, 200, 50
                                    )
    
    

    return ranking_armado


def dibujar_ranking(form_ranking):

    screen = pg.display.get_surface()
    screen.blit(var.RANKING_ESCALADO, (0, 0))

    form_ranking["lbl_titulo"].draw()
    form_ranking["lbl_subtitulo"].draw()

    for lbl in form_ranking["labels_top10"]:
        lbl.draw()

    fun.draw_button(screen, form_ranking.get("btn_volver"))

def obtener_tops(ruta_csv: str):
    matriz = []

    with open(ruta_csv, "r", encoding="utf-8") as file:
        contenido = file.read().strip()         
        lineas = contenido.split("\n")           

    for i in range(1, len(lineas)):
        linea = lineas[i]
        partes = linea.split(",")              

        if len(partes) != 2:
            continue 

        nombre = partes[0]
        puntaje = int(partes[1])
        matriz.append([nombre, puntaje])

    tops_ordenados = ordenar_tops(matriz)
    top10 = tops_ordenados[:10]
    return top10

def ordenar_tops(matriz):
    n = len(matriz)

    for i in range(n):
    
        for j in range(0, n - i - 1):
            
            if matriz[j][1] < matriz[j + 1][1]:  
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
    
    return matriz


def volver_menu(form_controlador, form_ranking, evento):
    if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
        mx, my = evento.pos

        if form_ranking["btn_volver"]['rect'].collidepoint(mx, my):
            form_controlador["lugar"] = "form_menu"



def guardar_puntaje_csv(path: str, nombre: str, puntaje: int) -> None:
    """Agrega un nuevo puntaje al CSV, creando el archivo si no existe.

    Args:
        path (str): Ruta del archivo CSV.
        nombre (str): Nombre del jugador.
        puntaje (int): Puntaje obtenido.
    """
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("Nombre,Puntaje\n")

    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{puntaje}\n")