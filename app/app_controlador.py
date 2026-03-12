from PySide6.QtWidgets import QApplication

from .ui.calculadora_modulo.ui_calculadora import UiInterfazCalculadora
from .ui.sesion_ui.ui_interfaz_sesion import UiInterfazSesion
from .ui.sesion_ui.ui_interfaz_registro import UiInterfazRegistro
from .ui.interfaz_principal_modulo.ui_interfaz_principal import UiInterfazPrincipal


class AppControlador:

    def __init__(self):
        self.app = QApplication([])

        self.calculadora_interfaz = None

        self.sesion_interfaz = None
        self.registro_interfaz = None
        self.interfaz_principal = None

    def iniciar(self):
        self.mostrar_calculadora()
        return self.app.exec()

    def mostrar_calculadora(self):
        self.calculadora_interfaz = UiInterfazCalculadora()

        self.calculadora_interfaz.iniciar_sistema.connect(self.mostrar_inicio)

        self.calculadora_interfaz.show()

    def mostrar_inicio(self):
        self.calculadora_interfaz.close()

        self.sesion_interfaz = UiInterfazSesion()

        self.sesion_interfaz.necesita_registro.connect(self.mostrar_registro)

        self.sesion_interfaz.inicio_satisfactorio.connect(
            self.mostrar_interfaz_principal
        )

        self.sesion_interfaz.show()

    def mostrar_registro(self):
        self.sesion_interfaz.close()

        self.registro_interfaz = UiInterfazRegistro()

        # señal para volver al login
        self.registro_interfaz.registro_cancelado.connect(self.volver_a_sesion)

        # señal si registro fue exitoso
        self.registro_interfaz.registro_exitoso.connect(self.volver_a_sesion)

        self.registro_interfaz.show()

    def volver_a_sesion(self):
        self.registro_interfaz.close()
        self.mostrar_inicio()

    def mostrar_interfaz_principal(self):
        if self.sesion_interfaz:
            self.sesion_interfaz.close()

        if self.registro_interfaz:
            self.registro_interfaz.close()

        self.interfaz_principal = UiInterfazPrincipal()
        self.interfaz_principal.show()
