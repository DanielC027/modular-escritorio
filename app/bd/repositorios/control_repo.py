from ..modelos import (
    obtener_control_crypto,
    actualizar_control_crypto,
    eliminar_control_crypto,
    es_tabla_vacia_control_crypto,
)


def obtener_control(id_usuario):
    return obtener_control_crypto(id_usuario)


def es_tabla_vacia_controlcrypto():
    return es_tabla_vacia_control_crypto()


def actualizar_control(id_usuario, payload_a, iv_a, payload_b, iv_b):
    actualizar_control_crypto(id_usuario, payload_a, iv_a, payload_b, iv_b)


def eliminar_control(id_usuario):
    eliminar_control_crypto(id_usuario)
