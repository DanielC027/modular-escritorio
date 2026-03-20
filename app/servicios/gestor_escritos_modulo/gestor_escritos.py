from datetime import date

from ...bd.repositorios.usuario_repo import (
    obtener_usuario_por_usuario,
    mostrar_usuario_por_id,
)
from ...bd.repositorios.escrito_repo import crear_escrito
from ...nucleo.encriptacion_modulo.AES_modulo import AESCifrado

import base64


class GestorEscritos:
    def __init__(self):
        self.aes_modulo = AESCifrado()

    def GuardarEscrito(self, fecha: date, contenido, datos):
        # Encriptar escrito
        # Generar huella digital
        # Guardar escrito
        datos_usuario = obtener_usuario_por_usuario(datos["usuario"])
        print(datos_usuario)
        print(datos)
        print(f"fecha: {fecha}, contenido: {contenido}")
        print(
            datos["contrasena"].encode()
        )  # continuar con la creacion y almacenamiento de huella digital, para despues
        # guardar los escritos completamente, todo el escrito, luego crear la lectura, creacion, y eliminacion de escritos
        print(
            base64.b64encode(
                (self.aes_modulo.generar_HMAC(datos["contrasena"].encode(), "hmac"))
            )
        )
        # base64.b64encode(sal).decode()

    def LeerEscrito(self):
        pass

    def ActualizarEscrito(self):
        pass

    def EliminarEscrito(self):
        pass

    def MostrarListaEscritos(self):
        pass
