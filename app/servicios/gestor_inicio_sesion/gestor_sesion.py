from ...bd.repositorios.usuario_repo import (
    obtener_usuario_por_usuario,
    es_tabla_vacia_usuario,
)
from ...bd.repositorios.control_repo import es_tabla_vacia_controlcrypto


class GestorSesion:
    def IniciarSesion(self, usuario, contrasena):
        """Intentar iniciar sesion"""
        ESTADO = {"SIN_REGISTRO": 0, "AUTENTICADO": 1, "NO_AUTENTICADO": 2}
        # Revisar si existe usuario y control de criptografia creados en la bd
        if es_tabla_vacia_usuario() or es_tabla_vacia_controlcrypto():
            # Si no existe regresar REGISTRO
            return ESTADO["SIN_REGISTRO"]

        # Obtener usuario por usuario sal, payload_a, iv_a, payload_b, iv_b de la bd
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
        # Obtener datos criptograficos
        # id_usuario = obtener_usuario_por_usuario(usuario)
        # generar payload aleatorio
        # datos_crypto = encriptar
        # Registrar usuario crypto_datos
        print(
            f"id_usuario: {usuario}, contrasena: {contrasena_1}, contrasena_2: {contrasena_2}"
        )
        pass
