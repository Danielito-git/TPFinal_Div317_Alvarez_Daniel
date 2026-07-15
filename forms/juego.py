import pygame as pg
import funciones as fun
import variablesyconst as var
import random
import os
import json
from utn_fra.pygame_widgets import Label



def form_juego(datos_iniciales: dict)->dict:
    juego_armado = {}
    mazo_jugador = crear_mazo_por_distribucion(cargar_cartas(var.CARTAS), var.distribucion)
    reverso_jugador = cargar_reverso_desde_mazo(mazo_jugador, (140,200))
    mazo_enemigo = crear_mazo_por_distribucion(cargar_cartas(var.CARTAS), var.distribucion)
    reverso_enemigo = cargar_reverso_desde_mazo(mazo_enemigo, (140,200))
    stats_jugador = fun.calcular_stats_mazo(mazo_jugador)
    stats_enemigo = fun.calcular_stats_mazo(mazo_enemigo)

    datos_iniciales["stats_jugador"] = stats_jugador
    datos_iniciales["stats_enemigo"] = stats_enemigo

    datos_iniciales["vida_jugador"] = stats_jugador["hp"]
    datos_iniciales["vida_enemigo"] = stats_enemigo["hp"]

    datos_iniciales["vida_max_jugador"] = stats_jugador["hp"]
    datos_iniciales["vida_max_enemigo"] = stats_enemigo["hp"]

    datos_iniciales["wishes_usados"] = {"heal": False, "shield": False}

    datos_iniciales["tiempo_restante_ms"] = var.TIMER_JUEGO * 1000
    datos_iniciales["ultimo_tick_ms"] = pg.time.get_ticks()

    screen = datos_iniciales["screen"]

    print("STATS JUGADOR:", datos_iniciales["stats_jugador"])
    print("STATS ENEMIGO:", datos_iniciales["stats_enemigo"])

    juego_armado["lugar"] = "form_juego"
    juego_armado["screen"] = screen
    juego_armado["conf_musica"] = datos_iniciales.get("conf_musica")
    juego_armado["mazo_jugador"] = mazo_jugador
    juego_armado["mazo_enemigo"] = mazo_enemigo
    juego_armado["musica_path"] = var.FORMS_MUSICA["form_juego"],
    juego_armado["fondo"] = var.JUEGO_ESCALADO
    juego_armado["conf_musica"] = datos_iniciales.get("conf_musica"),
    juego_armado["reverso_jugador"] = reverso_jugador
    juego_armado["reverso_enemigo"] = reverso_enemigo
    juego_armado["escala_carta"] = (140, 200)
    juego_armado["offset_mazo"] = 2

    fuente_letra = pg.font.Font(var.FUENTELETRA, 25)
    ancho, alto = var.PANTALLA

    # ---------- LABELS SUPERIORES ----------
    juego_armado['lbl_timer'] = Label(
        x=50, y=25,
        text=obtener_tiempo_str(datos_iniciales),
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=45,
        color=var.colores["cian"]
    )

    juego_armado['lbl_score'] = Label(
        x=430, y=25,
        text='Score: 0',
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=45,
        color=var.colores.get('cian')
    )

    juego_armado['lbl_carta_e'] = Label(
        x=390, y=275,
        text='',
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=20,
        color=var.colores["cian"]
    )

    juego_armado['lbl_carta_p'] = Label(
        x=390, y=563,
        text='',
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=25,
        color=var.colores["cian"]
    )

    # ---------- STATS ENEMIGO ----------
    juego_armado['lbl_enemigo_hp'] = Label(
        x=125, y=140,
        text="HP: 0",
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=20,
        color=var.colores["cian"]
    )

    juego_armado['lbl_enemigo_atk'] = Label(
        x=105, y=165,
        text='ATK: 0',
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=20,
        color=var.colores["cian"]
    )

    juego_armado['lbl_enemigo_def'] = Label(
        x=105, y=195,
        text='DEF: 0',
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=20,
        color=var.colores["cian"]
    )

    # ---------- STATS PLAYER ----------
    juego_armado['lbl_jugador_hp'] = Label(
        x=125, y=410,
        text="HP: 0",
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=20,
        color=var.colores["cian"]
    )

    juego_armado['lbl_jugador_atk'] = Label(
        x=105, y=440,
        text='ATK: 0',
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=20,
        color=var.colores["cian"]
    )

    juego_armado['lbl_jugador_def'] = Label(
        x=105, y=465,
        text='DEF: 0',
        screen=screen,
        font_path=var.FUENTELETRA,
        font_size=20,
        color=var.colores["cian"]
    )

    # ---------- BOTONES ----------
    juego_armado['btn_play'] = fun.crear_boton("Play",fuente_letra,var.colores["blanco"],var.colores["naranja"],
                                                725,300,w=50, h=50,
                                    )

    juego_armado['btn_heal'] = fun.crear_boton("Heal",fuente_letra,var.colores["blanco"],var.colores["naranja"],
                                                725,500,w=50, h=50,
                                    )
    
    juego_armado["lista_botones"] = [
        juego_armado['btn_heal'],
        juego_armado['btn_play']
    ]

    juego_armado['widgets_list'] = [
        juego_armado['lbl_timer'],
        juego_armado['lbl_score'],
        juego_armado['lbl_carta_e'],
        juego_armado['lbl_carta_p'],
        juego_armado['lbl_enemigo_hp'],
        juego_armado['lbl_enemigo_atk'],
        juego_armado['lbl_enemigo_def'],
        juego_armado['lbl_jugador_hp'],
        juego_armado['lbl_jugador_atk'],
        juego_armado['lbl_jugador_def'],
    ]

    return juego_armado

def cargar_cartas(path: str) -> list:
    """Carga un archivo JSON con cartas y devuelve la lista de cartas.

    Args:
        path (str): Ruta del archivo JSON.

    Returns:
        list: Lista de cartas (diccionarios).
    """
    if not os.path.isabs(path):
        path = os.path.join(var.PATH_PROYECTO, path)  

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def obtener_tiempo_str(form_controlador: dict) -> str:
    ms = form_controlador.get("tiempo_restante_ms", 0)
    total_seg = ms // 1000
    minutos = total_seg // 60
    segundos = total_seg % 60
    return f"{minutos:02d}:{segundos:02d}"

def dibujar_juego(form_juego: dict, datos_iniciales: dict):
    fun.actualizar_tiempo(datos_iniciales)
    fun.actualizar_labels_stats(form_juego, datos_iniciales)
    fun.actualizar_puntos(form_juego, datos_iniciales)
    
    form_juego['lbl_timer'].text = obtener_tiempo_str(datos_iniciales)
    fun.actualiza_label(form_juego['lbl_timer'])

    screen = form_juego['screen']
    screen.blit(var.JUEGO_ESCALADO, (0, 0))

    
    escala = form_juego["escala_carta"]

    carta_jugador = datos_iniciales.get("carta_jugador_actual")
    carta_enemigo = datos_iniciales.get("carta_enemigo_actual")

    x_mazos = 800 // 2 - 160
    x_carta = x_mazos + escala[0] + 10

    dibujar_mazo(
        screen,
        form_juego["reverso_enemigo"],
        len(form_juego["mazo_enemigo"]),
        x_mazos,
        110,
        escala
    )
    dibujar_mazo(
        screen,
        form_juego["reverso_jugador"],
        len(form_juego["mazo_jugador"]),
        x_mazos,
        380,
        escala
    )

    if carta_enemigo:
        img = cargar_frente_carta(carta_enemigo, escala)
        if img:
            pos = (x_carta, 110 )
            screen.blit(img, pos)
    
    if carta_jugador:
        img = cargar_frente_carta(carta_jugador, escala) 
        if img:
            pos = (x_carta,380 )
        
            screen.blit(img, pos)
    
    for boton in form_juego["lista_botones"]:
        fun.draw_button(screen, boton)

    for widget in form_juego['widgets_list']:
        widget.draw()


def actualizar_juego(datos_iniciales, eventos=None):
    if "form_juego" not in datos_iniciales:
        datos_iniciales["form_juego"] = form_juego(datos_iniciales)

    form_juego_data = datos_iniciales["form_juego"]

    if datos_iniciales.get("juego_terminado"):
        return

    dibujar_juego(form_juego_data, datos_iniciales)

    if eventos:
        for eve in eventos:
            if eve.type == pg.MOUSEBUTTONDOWN and eve.button == 1:
                boton_play = form_juego_data["btn_play"]
                if boton_play["rect"].collidepoint(eve.pos):
                    datos_iniciales["jugar_pendiente"] = True

                boton_heal = form_juego_data["btn_heal"]
                usados = datos_iniciales.get("wishes_usados", {})

                if boton_heal["rect"].collidepoint(eve.pos) and not (usados.get("heal") and usados.get("shield")):
                    datos_iniciales["lugar"] = "form_wish_confirm"

    if datos_iniciales.get("jugar_pendiente"):
        ejecutar_jugada(form_juego_data, datos_iniciales)
        datos_iniciales["jugar_pendiente"] = False


def crear_mazo_por_distribucion(cartas, distribucion):
    mazo = []

    for color, cantidad in distribucion.items():
        cartas_color = [c for c in cartas if color in c["serie"]]
            
        mazo.extend(random.sample(cartas_color, cantidad))
        #random.shuffle(mazo)
            
    return mazo

def cargar_reverso_desde_mazo(mazo, escala):
    if not mazo:
        return None

    
    ruta_relativa = mazo[0]["ruta_reverso"].replace("\\", "/")
    ruta = os.path.join(var.PATH_PROYECTO, ruta_relativa)

    if not os.path.exists(ruta):
        print("Reverso no encontrado:", ruta)
        return None

    imagen = pg.image.load(ruta).convert_alpha()
    return pg.transform.scale(imagen, escala)

def dibujar_mazo(screen, img_reverso, cantidad, x, y, escala):
    if cantidad <= 0:
        return

    if img_reverso:
        screen.blit(img_reverso, (x, y))
    else:
        pg.draw.rect(
            screen,
            (200, 50, 50),
            (x, y, escala[0], escala[1]),
            2
        )

def cargar_frente_carta(carta, escala):
    ruta = os.path.join(var.PATH_PROYECTO, carta["ruta_frente"]) 

    if not os.path.exists(ruta):
        print("❌ Frente no encontrado:", ruta)
        return None

    img = pg.image.load(ruta).convert_alpha()
    return pg.transform.scale(img, escala)

def agarrar_carta(mazo):
    if len(mazo) == 0:
        return None
    return mazo.pop(0)

def calcular_ataque_efectivo(carta: dict) -> float:
    bonus = 1 + (carta["bonus"] * var.BONUS_POR_ESTRELLA)
    return carta["atk"] * bonus

def calcular_penalizacion(carta: dict) -> dict:
    bonus = 1 + (carta["estrellas"] * var.BONUS_POR_ESTRELLA)

    return {
        "hp": carta["hp"] * bonus,
        "atk": carta["atk"] * bonus,
        "def": carta["def"] * bonus
    }

def ejecutar_wish(datos):
    wishes = datos.get("wishes", {})

    if wishes.get("heal"):
        datos["vida_jugador"] += datos.get("vida_max_jugador", 0)
        wishes["heal"] = False

    if wishes.get("shield"):
        datos["shield_activo"] = True
        wishes["shield"] = False

    return datos


def ejecutar_jugada(form_juego, datos_iniciales):

    if datos_iniciales.get("juego_terminado"):
        return

    mazo_j = form_juego["mazo_jugador"]
    mazo_e = form_juego["mazo_enemigo"]

    if not mazo_j or not mazo_e:
        datos_iniciales["juego_terminado"] = True
        return

    carta_j = mazo_j.pop(0)
    carta_e = mazo_e.pop(0)

    datos_iniciales["carta_jugador_actual"] = carta_j
    datos_iniciales["carta_enemigo_actual"] = carta_e

    atk_j = calcular_ataque_efectivo(carta_j)
    atk_e = calcular_ataque_efectivo(carta_e)

    ejecutar_wish(datos_iniciales)

    if atk_j > atk_e:
        perdedor = "enemigo"
        puntos = 100 * carta_j.get("bonus")
        fun.sumar_puntos(datos_iniciales, int(puntos))
        print("victoria")
    elif atk_e > atk_j:
        perdedor = "jugador"
        print("derrota")
    else:
        perdedor = "empate"
        print("empate")

    damage = 0

    if perdedor != "empate":
        damage = fun.aplicar_damage(
            perdedor,
            carta_j,
            carta_e,
        )

        if perdedor == "jugador" and datos_iniciales.get("shield_activo"):
            print("SHIELD ACTIVADO → DAÑO AL ENEMIGO")
            datos_iniciales["vida_enemigo"] -= 2*damage
            datos_iniciales["shield_activo"] = False
        else:
            if perdedor == "jugador":
                datos_iniciales["vida_jugador"] -= 2*damage
            else:
                datos_iniciales["vida_enemigo"] -= 2*damage

    if datos_iniciales["vida_jugador"] <= 0:
        datos_iniciales["juego_terminado"] = True
        datos_iniciales["ganador"] = "enemigo"
        datos_iniciales["lugar"] = "form_game_over"
        print("GANA ENEMIGO")

    if datos_iniciales["vida_enemigo"] <= 0:
        datos_iniciales["juego_terminado"] = True
        datos_iniciales["ganador"] = "jugador"
        datos_iniciales["lugar"] = "form_game_over"
        print("GANA JUGADOR")
    
    return datos_iniciales
