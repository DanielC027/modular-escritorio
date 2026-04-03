from ..modelos import (
    crear_analisis,
    revisar_existe_analisis,
    obtener_id_analisis_por_id_escrito,
)


def crear_analisis_escrito(id_escrito):
    crear_analisis(id_escrito)


def revisar_existe_analisis_en_bd(id_escrito):
    return revisar_existe_analisis(id_escrito)


def obtener_id_analisis(id_escrito):
    return obtener_id_analisis_por_id_escrito(id_escrito)
