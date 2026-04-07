from ..modelos import (
    crear_emocion,
    crear_analisis,
    revisar_existe_analisis,
    obtener_id_analisis_por_id_escrito,
    obtener_id_emocion_bd,
    existe_emocion_bd,
    existe_lista_emociones_bd,
    existe_emocion_de_analisis,
    agregar_emocion_a_analisis,
    actualizar_emocion_de_analisis,
)


def crear_analisis_escrito(id_escrito):
    crear_analisis(id_escrito)


def revisar_existe_analisis_en_bd(id_escrito):
    return revisar_existe_analisis(id_escrito)


def obtener_id_analisis(id_escrito):
    return obtener_id_analisis_por_id_escrito(id_escrito)


# --------------------------------------------------------------


def crear_una_emocion(emocion):
    return crear_emocion(emocion)


def existe_emocion(nombre):
    return existe_emocion_bd(nombre)


def obtener_id_emocion(emocion):
    return obtener_id_emocion_bd(emocion)


# --------------------------------------------------------------


def existe_lista_emociones(id_analisis):
    return existe_lista_emociones_bd(id_analisis)


def existe_emocion_en_analisis(id_analisis, id_emocion):
    return existe_emocion_de_analisis(id_analisis, id_emocion)


def agregar_emocion_al_analisis(id_analisis, id_emocion, porcentaje):
    agregar_emocion_a_analisis(id_analisis, id_emocion, porcentaje)


def actualizar_emocion_del_analisis(id_analisis, id_emocion, porcentaje):
    actualizar_emocion_de_analisis(id_analisis, id_emocion, porcentaje)
