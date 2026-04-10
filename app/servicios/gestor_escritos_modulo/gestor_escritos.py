from datetime import date

from ...bd.repositorios.usuario_repo import (
    obtener_usuario_por_usuario,
)
from ...bd.repositorios.escrito_repo import (
    crear_escrito,
    mostrar_lista_escritos,
    existe_fecha_guardada,
    obtener_escrito,
    obtener_id_escrito,
    actualizar_contenido,
    eliminar_escrito_usuario,
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
            huella_digital_bd = self.GenerarHuellaDigital(datos)
            # print(huella_digital_bd)
            # Enviar datos para la bd tabla escrito para crear uno
            crear_escrito(
                id_usuario_bd, fecha_bd, contenido_bd, iv_bd, huella_digital_bd
            )
            return True
        except Exception as ex:
            print(ex)
            return False

    def LeerEscrito(self, fecha, datos):
        try:
            # ===== Generar huella digital =====
            huella_digital_bd = self.GenerarHuellaDigital(datos)
            print(huella_digital_bd)
            # ===== Obtener escrito =====
            fecha_bd = fecha
            # print(f"Leer escrito - Gestor escritos - {huella_digital_bd} {fecha}")
            contenido = obtener_escrito(huella_digital_bd, fecha_bd)
            # obtener formato
            sal_contenido_bd, nonce_contenido_bd, texto_contenido_bd = contenido[
                "CONTENIDO"
            ].split("|")
            tag_bd = contenido["IV"]
            datos_bd = {
                "sal": sal_contenido_bd,
                "nonce": nonce_contenido_bd,
                "tag": tag_bd,
                "texto": texto_contenido_bd,
            }
            # print(datos_bd)
            contenido_desencriptado = self.aes_modulo.desencriptar(
                datos["contrasena"], datos_bd
            )
            # print(f" contenido desencriptado bd: {contenido_desencriptado}")

            return contenido_desencriptado
        except Exception as ex:
            print(ex)
            return ""

    def ActualizarEscrito(self, fecha, contenido, datos):
        try:
            # ===== Encriptar escrito =====
            contenido_encriptado = self.aes_modulo.encriptar(
                datos["contrasena"], contenido
            )
            # ===== Actualizar escrito =====
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
            huella_digital_bd = self.GenerarHuellaDigital(datos)

            # Enviar datos para la bd tabla escrito para actualizar el escrito
            actualizar_contenido(
                id_usuario_bd, fecha_bd, contenido_bd, iv_bd, huella_digital_bd
            )
            return True
        except Exception as ex:
            print(ex)
            return False

    def EliminarEscrito(self, fecha, datos):
        try:
            # ===== Generar huella digital =====
            huella_digital_bd = self.GenerarHuellaDigital(datos)
            # ===== Eliminar escrito =====
            # Eliminar el escrito que corresponde a la fecha y a la huella digital
            resultado = eliminar_escrito_usuario(fecha, huella_digital_bd)
            return resultado
        except Exception as ex:
            print(ex)
            return False

    def MostrarListaEscritos(self, datos):
        try:
            # ===== Generar huella digital =====
            huella_digital_bd = self.GenerarHuellaDigital(datos)
            # ===== Buscar escritos =====
            # Buscar todos los escritos que corresponden a la huella digital
            escritos = mostrar_lista_escritos(huella_digital_bd)
            # print(huella_digital_bd)
            for escrito in escritos:
                print(" ", escrito["FECHA"])

            lista_fechas = [escrito["FECHA"] for escrito in escritos]
            # print(lista_fechas)
            return lista_fechas
        except Exception as ex:
            print(ex)
            return []

    def RevisarExisteFechaGuardada(self, fecha, datos):
        try:
            huella_digital_bd = self.GenerarHuellaDigital(datos)
            # ===== Buscar existencia de escrito =====
            return existe_fecha_guardada(huella_digital_bd, fecha)
        except Exception as ex:
            print(ex)
            return False

    def ObtenerIDEscrito(self, fecha, datos):
        try:
            huella_digital_bd = self.GenerarHuellaDigital(datos)
            # ===== Buscar existencia de escrito =====
            return obtener_id_escrito(huella_digital_bd, fecha)
        except Exception as ex:
            print(ex)
            return -1

    def GenerarHuellaDigital(self, datos):
        # ===== Generar huella digital =====
        clave_generada_huella_digital = self.aes_modulo.generar_HMAC(
            datos["sal"].encode(), "hmac"
        )
        huella_digital = self.aes_modulo.generar_HMAC(
            clave_generada_huella_digital, "hmac"
        )
        return base64.b64encode(huella_digital)
