from ..modelos import (
    crear_escrito,
    obtener_escritos,
    actualizar_escrito,
    eliminar_escrito,
)


def crear_nuevo_escrito(id_usuario, fecha, contenido):
    crear_escrito(id_usuario, fecha, contenido)


def obtener_escritos_usuario(id_usuario):
    return obtener_escritos(id_usuario)


def actualizar_contenido_escrito(id_escrito, contenido):
    actualizar_escrito(id_escrito, contenido)


def eliminar_escrito_usuario(id_escrito):
    eliminar_escrito(id_escrito)
