import pygame as pg
import variablesyconst as var
import os


def crear_boton(text: str, font: pg.font.Font, txt_color: tuple, bg_color: tuple, x: int, y: int, w: int, h: int) -> dict:
    """Crea un boton con texto y colores dados

    Args:
        texto (str): Texto del boton.
        font (pg.font.Font): Fuente del texto.
        txt_color (tuple): Color del texto.
        bg_color (tuple): Color de fondo normal.
        x (int): Posicion horizontal.
        y (int): Posicion vertical.
        w (int): Ancho del boton.
        h (int): Alto del boton.

    Returns:
        dict: Diccionario que representa el boton
    """
    rect = pg.Rect(x, y, w, h)
    surf_text = font.render(text, True, txt_color)
    text_rect = surf_text.get_rect(center=rect.center)

    return {
        "type": "button",
        "rect": rect,
        "text": text,
        "text_surface": surf_text,
        "text_rect": text_rect,
        "bg_color": bg_color,
        "current_color": bg_color,
        "text_color": txt_color,
    }

def draw_button(screen: pg.Surface, button: dict):
    """Dibuja un boton en la pantalla.

    Args:
        screen (pg.Surface): Superficie donde dibujar el boton.
        button (dict): boton a dibujar.
    """
    pg.draw.rect(screen, button["current_color"], button["rect"], border_radius=10)
    screen.blit(button["text_surface"], button["text_rect"])

def actualiza_label(label):
    label.image = label.font.render(
        label.text,
        True,
        (0, 255, 255)
    )

def resetear_estado_juego(datos):
    # Gameplay
    datos["juego_terminado"] = False
    datos["ganador"] = None
    datos["jugar_pendiente"] = False
    datos["player"] = ""

    # Eliminar forms persistentes
    datos.pop("form_juego", None)
    datos.pop("form_game_over", None)

def sumar_puntos(datos: dict, puntos: int):
    datos["puntos_totales"] += 3*puntos

def actualizar_puntos(form_juego:dict, datos_iniciales:dict):
    form_juego["lbl_score"].text = f"Score: {datos_iniciales['puntos_totales']}"
    actualiza_label(form_juego["lbl_score"])
    

def actualizar_labels_stats(form_juego: dict, datos_iniciales: dict):

    stats_j = datos_iniciales["stats_jugador"]
    stats_e = datos_iniciales["stats_enemigo"]

    vida_j = datos_iniciales["vida_jugador"]
    vida_e = datos_iniciales["vida_enemigo"]

    # ENEMIGO
    lbl = form_juego["lbl_enemigo_hp"]
    lbl.text = f"HP: {int(vida_e)}"
    actualiza_label(lbl)

    lbl = form_juego["lbl_enemigo_atk"]
    lbl.text = f"ATK: {int(stats_e['atk'])}"
    actualiza_label(lbl)

    lbl = form_juego["lbl_enemigo_def"]
    lbl.text = f"DEF: {int(stats_e['def'])}"
    actualiza_label(lbl)

    # JUGADOR
    lbl = form_juego["lbl_jugador_hp"]
    lbl.text = f"HP: {int(vida_j)}"
    actualiza_label(lbl)

    lbl = form_juego["lbl_jugador_atk"]
    lbl.text = f"ATK: {int(stats_j['atk'])}"
    actualiza_label(lbl)

    lbl = form_juego["lbl_jugador_def"]
    lbl.text = f"DEF: {int(stats_j['def'])}"
    actualiza_label(lbl)

def calcular_stats_mazo(mazo):
    hp = atk = deff = 0
    for carta in mazo:
        hp += carta.get("hp", 0)
        atk += carta.get("atk", 0)
        deff += carta.get("def", 0)
    return {
        "hp": int(hp),
        "atk": int(atk),
        "def": int(deff)
    }


def actualizar_tiempo(datos_iniciales: dict) -> dict:
    ahora = pg.time.get_ticks()
    ultimo = datos_iniciales.get("ultimo_tick_ms", ahora)

    transcurridos = ahora - ultimo   # ms transcurridos desde el último frame
    datos_iniciales["ultimo_tick_ms"] = ahora

    restante = datos_iniciales.get("tiempo_restante_ms", 0)
    restante -= transcurridos
    if restante < 0:
        restante = 0

    datos_iniciales["tiempo_restante_ms"] = restante
    return datos_iniciales


def aplicar_damage(perdedor: str, carta_j: dict, carta_e:dict):
    if perdedor == "enemigo":
        damage = carta_j["atk"] + carta_j.get("bonus", 0)
        print(f"Daño aplicado a enemigo: {damage}")
        return int(damage)

    elif perdedor == "jugador":
        damage = carta_e["atk"] + carta_e.get("bonus", 0)
        print(f"Daño aplicado a jugador: {damage}")
        return int(damage)

    print(f"Daño aplicado a {perdedor}: {damage}")
    return 0  

def calcular_stats_mazo(mazo: list) -> dict:
    stats = {
        "hp": 0,
        "atk": 0,
        "def": 0
    }

    for carta in mazo:
        stats["hp"] += carta.get("hp", 0)
        stats["atk"] += carta.get("atk", 0)
        stats["def"] += carta.get("def", 0)

    return stats
