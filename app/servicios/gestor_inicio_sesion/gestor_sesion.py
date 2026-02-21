from ...bd.repositorios.usuario_repo import (
    registrar_usuario,
    obtener_usuario_por_usuario,
    es_tabla_vacia_usuario,
    mostrar_usuario_por_id,
)
from ...bd.repositorios.control_repo import (
    obtener_control,
)

from ...bd.repositorios.control_repo import es_tabla_vacia_controlcrypto
from ...nucleo.encriptacion_modulo.AES_modulo import AESCifrado


class GestorSesion:
    def IniciarSesion(self, usuario, contrasena):
        """Intentar iniciar sesion"""
        ESTADO = {"SIN_REGISTRO": 0, "AUTENTICADO": 1, "NO_AUTENTICADO": 2}
        USUARIO = {"ID_USUARIO": 0, "USUARIO": 1, "SAL": 2}
        CRYPTO = {
            "ID_CRYPTO": 0,
            "ID_USUARIO": 1,
            "PAYLOAD_A": 2,
            "IV_A": 3,
            "PAYLOAD_B": 4,
            "IV_B": 5,
        }
        # Revisar si existe usuario y control de criptografia creados en la bd
        if es_tabla_vacia_usuario() or es_tabla_vacia_controlcrypto():
            # Si no existe regresar REGISTRO
            return ESTADO["SIN_REGISTRO"]

        # Obtener usuario por usuario sal, payload_a, iv_a, payload_b, iv_b de la bd
        id_persona = obtener_usuario_por_usuario(usuario)

        datos_persona = mostrar_usuario_por_id(id_persona)
        print(
            "datos persona: ",
            datos_persona[USUARIO["USUARIO"]],
            " ",
            datos_persona[USUARIO["SAL"]],
        )

        datos_control_crypto = obtener_control(id_persona)
        print(
            f"datso crypto: {datos_control_crypto[CRYPTO["ID_CRYPTO"]]} {datos_control_crypto[CRYPTO["ID_USUARIO"]]} {datos_control_crypto[CRYPTO["PAYLOAD_A"]]} {datos_control_crypto[CRYPTO["IV_A"]]} {datos_control_crypto[CRYPTO["PAYLOAD_B"]]} {datos_control_crypto[CRYPTO["IV_B"]]}  "
        )
        # Intentar desencriptar payloads
        print(
            f"INICIAR SESION - REVISAR CREDENCIALES: usuario - {usuario} , contaseña - {contrasena}"
        )
        # si se desencripta alguno - pasar, si no, usuario o contraseña no validos
        # Si desencripta payload regresar satisfactorio - ESTADO["AUTENTICADO"]
        # Si no desencripta payload regresar NO satisfactorio - ESTADO["NO_AUTENTICADO"]
        pass

    def RegistrarUsuario(self, usuario, contrasena_1, contrasena_2):
        """Registrar usuario"""
        encripta_modulo = AESCifrado()
        # --- Obtener datos criptograficos ---
        # generar payload aleatorio
        payload_1 = encripta_modulo.obtener_payload_aleatorio()
        payload_2 = encripta_modulo.obtener_payload_aleatorio()

        datos_1_crypto = encripta_modulo.encriptar(contrasena_1, payload_1)
        datos_2_crypto = encripta_modulo.encriptar(contrasena_2, payload_2)

        print(datos_1_crypto)
        print(datos_2_crypto)

        #   USUARIO - usuario, sal
        sal = datos_1_crypto["sal"] + "|" + datos_2_crypto["sal"]

        #   CONTROL_CRYPTO
        # iv 1 (nonce), tag 1 + payload 1
        nvo_payload_1 = datos_1_crypto["tag"] + "|" + datos_1_crypto["texto"]
        nvo_iv_1 = datos_1_crypto["nonce"]
        # iv 2 (nonce), tag 2 + payload 2
        nvo_payload_2 = datos_2_crypto["tag"] + "|" + datos_2_crypto["texto"]
        nvo_iv_2 = datos_2_crypto["nonce"]

        datos_crypto = {
            "sal": sal,
            "payload_a": nvo_payload_1,
            "iv_a": nvo_iv_1,
            "payload_b": nvo_payload_2,
            "iv_b": nvo_iv_2,
        }
        # Registrar usuario crypto_datos
        registrar_usuario(usuario, datos_crypto)

        print(
            f"id_usuario: {usuario}, contrasena: {contrasena_1}, contrasena_2: {contrasena_2}, | py1: {payload_1}, py2: {payload_2}"
        )
