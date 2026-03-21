from datetime import date

from ...bd.repositorios.usuario_repo import (
    obtener_usuario_por_usuario,
)
from ...bd.repositorios.escrito_repo import (
    crear_escrito,
    mostrar_lista_escritos,
)
from ...nucleo.encriptacion_modulo.AES_modulo import AESCifrado

import base64


class GestorEscritos:
    def __init__(self):
        self.aes_modulo = AESCifrado()

    def GuardarEscrito(self, fecha: date, contenido, datos):
        try:
            # ===== Encriptar escrito =====
            contenido_encriptado = self.aes_modulo.encriptar(
                datos["contrasena"], contenido
            )
            # print(contenido_encriptado)
            # ===== Generar huella digital =====
            clave_generada_huella_digital = self.aes_modulo.generar_HMAC(
                datos["sal"].encode(), "hmac"
            )
            huella_digital = self.aes_modulo.generar_HMAC(
                clave_generada_huella_digital, "hmac"
            )
            # ===== Guardar escrito =====
            id_usuario_bd = obtener_usuario_por_usuario(datos["usuario"])
            fecha_bd = fecha
            contenido_bd = (
                contenido_encriptado["sal"]
                + "|"
                + contenido_encriptado["nonce"]
                + "|"
                + contenido_encriptado["texto"]
            )
            iv_bd = contenido_encriptado["tag"]
            huella_digital_bd = base64.b64encode(huella_digital)
            print(huella_digital_bd)
            # Enviar datos para la bd tabla escrito para crear uno
            crear_escrito(
                id_usuario_bd, fecha_bd, contenido_bd, iv_bd, huella_digital_bd
            )
            return True
        except Exception as ex:
            print(ex)
            return False

    def LeerEscrito(self):
        pass

    def ActualizarEscrito(self):
        pass

    def EliminarEscrito(self):
        pass

    def MostrarListaEscritos(self, datos):
        try:
            # ===== Generar huella digital =====
            clave_generada_huella_digital = self.aes_modulo.generar_HMAC(
                datos["sal"].encode(), "hmac"
            )
            huella_digital = self.aes_modulo.generar_HMAC(
                clave_generada_huella_digital, "hmac"
            )
            huella_digital_bd = base64.b64encode(huella_digital)
            # ===== Buscar escritos =====
            # Buscar todos los escritos que corresponden a la huella digital
            escritos = mostrar_lista_escritos(huella_digital_bd)
            print(huella_digital_bd)
            for escrito in escritos:
                print(escrito["ID_ESCRITO"], " ", escrito["FECHA"])
            return True
        except Exception as ex:
            print(ex)
            return False
