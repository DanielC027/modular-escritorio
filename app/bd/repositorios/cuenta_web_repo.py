from ..modelos import (
    crear_cuenta_web,
    obtener_cuentas_web,
    eliminar_cuenta_web,
)


def registrar_cuenta_web(id_usuario, id_opaque):
    crear_cuenta_web(id_usuario, id_opaque)


def obtener_cuentas_usuario(id_usuario):
    return obtener_cuentas_web(id_usuario)


def eliminar_cuenta(id_cuenta_web):
    eliminar_cuenta_web(id_cuenta_web)
