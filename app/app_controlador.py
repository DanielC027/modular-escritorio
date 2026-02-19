from PySide6.QtWidgets import QApplication

# from .ui.sesion_ui.registro_mainwindow_ui import Ui_RegistroMainWindow
from .ui.sesion_ui.ui_interfaz_sesion import UiInterfazSesion


class AppControlador:

    def __init__(self):
        self.app = QApplication([])
        self.sesion_interfaz = None
        self.registro_interfaz = None
        self.interfaz_principal = None

    def iniciar(self):
        self.mostrar_inicio()
        return self.app.exec()

    def mostrar_inicio(self):
        self.sesion_interfaz = UiInterfazSesion()

        # self.sesion_interfaz.inicio_satisfactorio.connect(self.mostrar_interfaz_principal)
        self.sesion_interfaz.show()

    def mostrar_registro(self):
        pass

    def mostrar_interfaz_principal(self):
        self.sesion_interfaz.close()
        # self.interfaz_principal = UiInterfazPrincipal()
        self.interfaz_principal.show()
