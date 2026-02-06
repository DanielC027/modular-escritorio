from ..modelos import crear_analisis


def crear_analisis_escrito(id_escrito, fecha):
    """
    Devuelve el ID del análisis creado
    """
    return crear_analisis(id_escrito, fecha)
