from ..modelos import (
    crear_emocion,
    agregar_emocion_a_analisis,
    obtener_emociones_de_analisis,
)


def registrar_emocion(nombre):
    crear_emocion(nombre)


def agregar_emocion_analisis(id_analisis, id_emocion, porcentaje):
    agregar_emocion_a_analisis(id_analisis, id_emocion, porcentaje)


def obtener_emociones_analisis(id_analisis):
    return obtener_emociones_de_analisis(id_analisis)
