from ..modelos import (
    crear_escrito,
    obtener_escritos,
    actualizar_escrito,
    eliminar_escrito,
    mostrar_lista_escritos_en_bd,
    revisar_existe_fecha_guardada,
    obtener_escrito_de_bd,
    obtener_id_escrito_bd,
)


def crear_nuevo_escrito(id_usuario, fecha, contenido, iv, huella_digital):
    crear_escrito(id_usuario, fecha, contenido, iv, huella_digital)


def obtener_escritos_usuario(id_usuario):
    return obtener_escritos(id_usuario)


def obtener_escrito(huella_digital, fecha):
    return obtener_escrito_de_bd(huella_digital, fecha)


def obtener_id_escrito(huella_digital, fecha):
    return obtener_id_escrito_bd(huella_digital, fecha)


def actualizar_contenido(id_usuario, fecha, contenido, iv, huella_digital):
    actualizar_escrito(id_usuario, fecha, contenido, iv, huella_digital)


def eliminar_escrito_usuario(fecha, huella_digital):
    return eliminar_escrito(fecha, huella_digital)


def mostrar_lista_escritos(huella_digital):
    return mostrar_lista_escritos_en_bd(huella_digital)


def existe_fecha_guardada(huella_digital, fecha):
    return revisar_existe_fecha_guardada(huella_digital, fecha)
