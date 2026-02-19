from ...bd.repositorios.usuario_repo import obtener_usuario_por_usuario


class GestorSesion:
    def IniciarSesion(self, usuario, contrasena):
        """Intentar iniciar sesion"""
        # Obtener usuario por usuario
        id_usuario = obtener_usuario_por_usuario(usuario)
        print("id_usuario: ", id_usuario, "contrasena: ", contrasena)
        # Si desencripta payload regresar satisfactorio
        # Si no desencripta payload regresar NO satisfactorio
        # Si no existe regresar REGISTRO
        pass

    def RegistrarUsuario(self, usuario, contrasena_1, contrasena_2):
        """Registrar usuario"""
        # Obtener datos criptograficos
        # Registrar usuario crypto_datos
        pass
