import pygame as pg
import json

PANTALLA = 800, 600

FUENTELETRA = "assets/fuentes/alagard.ttf"
FUENTE_NUMERO = "assets/fuentes/Saiyan-Sans.ttf"

VIDASTOTALES = 3

volumen = 10
MIN_VOLUME = 1
MAX_VOLUME = 100
STEP_VOLUME = 5

BONUS_POR_ESTRELLA = 0.1

TIMER_JUEGO = 250

CARTAS = "todas_las_cartas.json"

distribucion = {
    "platinum": 1,
    "black": 2,
    "golden": 1,
    "silver": 3,
    "purple": 4,
    #"red": 6,
    #"blue": 8,
    #"green": 15
}

ICONOJUEGO = pg.image.load("assets/imagenes/fondos/HD-wallpaper-2d-pixel-art-medieval-background-pack.jpg")
fondo_menu = pg.image.load("assets/imagenes/fondos/fondo-menu.jpg")
MENUE_SCALADO = pg.transform.scale(fondo_menu, PANTALLA)

fondo_juego = pg.image.load("assets/imagenes/fondos/background_cards_simple.png")
JUEGO_ESCALADO = pg.transform.scale(fondo_juego, PANTALLA)

fondo_opciones = pg.image.load("assets/imagenes/fondos/form_options.png")
OPCIONES_ESCALADO = pg.transform.scale(fondo_opciones, PANTALLA)

fondo_ranking = pg.image.load("assets/imagenes/fondos/form_ranking.png")
RANKING_ESCALADO = pg.transform.scale(fondo_ranking, PANTALLA)

fondo_wish = pg.image.load("assets/imagenes/fondos/form_wish_select.png")
WISH_ESCALADO = pg.transform.scale(fondo_wish, PANTALLA)

fondo_tuto = pg.image.load("assets/imagenes/fondos/fondo-tuto.jpg")
TUTO_ESCALADO = pg.transform.scale(fondo_tuto, PANTALLA)

fondo_juego_victoria = pg.image.load("assets/imagenes/fondos/form_enter_name.png")
fondo_juego_derrota = pg.image.load("assets/imagenes/fondos/form_enter_name_0.png")
VICTORIA_ESCALADA = pg.transform.scale(fondo_juego_victoria, PANTALLA)
DERROTA_ESCALADA = pg.transform.scale(fondo_juego_derrota, PANTALLA)

colores = {
    "amarillo": pg.Color('yellow'),
    "azul": pg.Color('blue'),
    "blanco": pg.Color('white'),
    "cian": pg.Color('cyan'),
    "naranja": pg.Color('orange'),
    "negro": pg.Color('black'),
    "rojo": pg.Color('red'),
    "rosa": pg.Color('pink'),
    "verde": pg.Color("green")
}

imagen_tuto_1 = pg.image.load("assets/imagenes/tutorial/boton_play.png")
imagen_tuto_2 = pg.image.load("assets/imagenes/tutorial/wish_heal.png")
imagen_tuto_3 = pg.image.load("assets/imagenes/tutorial/wish_shield.png")
imagen_tuto_4 = pg.image.load("assets/imagenes/tutorial/juego_mano.png")
imagen_tuto_5 = pg.image.load("assets/imagenes/tutorial/final_juego.png")
imagen_tuto_6 = pg.image.load("assets/imagenes/tutorial/puntaje.png")
imagen_tuto_7 = pg.image.load("assets/imagenes/tutorial/timer.png")
imagen_tuto_8 = pg.image.load("assets/imagenes/tutorial/ranking.png")


FORMS_MUSICA = {
    "form_ranking": "assets/sonidos/form_ranking.ogg",
    "form_menu": "assets/sonidos/form_main_menu.ogg",
    "form_opciones": "assets/sonidos/form_options.ogg",
    #MUSICA_PAUSE = 'assets/sound/level_1.mp3',
    "form_juego": "assets/sonidos/level_01.ogg",
    "form_final_victoria": "assets/sonidos/win_music.ogg"
}
