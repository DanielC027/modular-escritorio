from ..modelos import (
    crear_usuario,
    obtener_usuario,
    actualizar_usuario,
    eliminar_usuario,
    obtener_usuario_por_usuario_registro,
    es_tabla_vacia_usuarios,
)


def registrar_usuario(usuario, crypto_datos):
    crear_usuario(usuario, crypto_datos)


def mostrar_usuario(id_usuario):
    return obtener_usuario(id_usuario)


def modificar_usuario(id_usuario, usuario, sal):
    actualizar_usuario(id_usuario, usuario, sal)


def eliminar_usuario_completamente(id_usuario):
    eliminar_usuario(id_usuario)


def obtener_usuario_por_usuario(usuario):
    return obtener_usuario_por_usuario_registro(usuario)


def es_tabla_vacia_usuario():
    return es_tabla_vacia_usuarios()
