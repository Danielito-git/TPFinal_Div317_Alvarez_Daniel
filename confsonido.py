import pygame.mixer as mixer
import variablesyconst as var
import pygame as pg



def iniciar_musica(volumen: int, musica_path):
    pg.mixer.music.load(musica_path)
    set_volume(volumen)
    pg.mixer.music.play(-1)

def get_actual_volumen() -> int:
    actual_vol = mixer.music.get_volume() * 100
    return int(actual_vol)


def set_volume(volumen: int):
    """Establece el volumen en porcentaje (0-100).

    Convierte a la escala que usa pygame (0.0 - 1.0).
    """

    if volumen < 0:
        volumen = 0
    if volumen > 100:
        volumen = 100

    actual_vol = volumen / 100.0
    mixer.music.set_volume(actual_vol)

def mute_desmute(form_controlador):
    estado = form_controlador["conf_musica"].get("apagada", False)

    if estado:
        # desmutear: restaurar volumen guardado
        volumen = form_controlador["conf_musica"].get("volumen", get_actual_volumen())
        set_volume(volumen)
        form_controlador["conf_musica"]["apagada"] = False
    else:
        # mutear
        set_volume(0)
        form_controlador["conf_musica"]["apagada"] = True

    return form_controlador

def modificar_volumen(delta: int, form_controlador: dict):
    """Modifica el volumen en `delta` (porcentaje) y lo aplica al mixer.

    Actualiza además `form_controlador['conf_musica']['volumen']`.
    """
    conf = form_controlador.get("conf_musica", {})
    vol_actual = conf.get("volumen", get_actual_volumen())

    vol_actual += int(delta)

    # aplicar límites solicitados
    if vol_actual < var.MIN_VOLUME:
        vol_actual = var.MIN_VOLUME
    if vol_actual > var.MAX_VOLUME:
        vol_actual = var.MAX_VOLUME

    # guardar y aplicar
    form_controlador.setdefault("conf_musica", {})["volumen"] = vol_actual
    set_volume(vol_actual)
    

def evento_mute_desmute(form_controlador, form_opciones, evento):
    if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
        mx, my = evento.pos

        if form_opciones["btn_musica"]["rect"].collidepoint(mx, my):
            mute_desmute(form_controlador)

def subir_bajar_vol(form_controlador, form_opciones, evento):
    if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
        mx, my = evento.pos
        eventito = mx, my

        if form_opciones["btn_mas"]["rect"].collidepoint(eventito):
            modificar_volumen(var.STEP_VOLUME, form_controlador)

        if form_opciones["btn_menos"]["rect"].collidepoint(eventito):
            modificar_volumen(-var.STEP_VOLUME, form_controlador)
            

def reproducir_musica_lugar(form_controlador: dict):
    lugar = form_controlador.get("lugar")

    ruta_deseada = var.FORMS_MUSICA.get(lugar)

    # configuracion de audio
    conf = form_controlador.get("conf_musica", {})
    volumen = conf.get("volumen", get_actual_volumen())
    apagada = conf.get("apagada", False)

    if ruta_deseada is None:
        return form_controlador

    if apagada:
        pg.mixer.music.set_volume(0)
        return form_controlador

    tema_actual = form_controlador.get("tema_actual")
    if tema_actual != ruta_deseada:
        iniciar_musica(volumen, ruta_deseada)
        form_controlador["tema_actual"] = ruta_deseada

    return form_controlador
