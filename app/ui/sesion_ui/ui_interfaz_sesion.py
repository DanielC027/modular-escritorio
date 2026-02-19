from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from .sesion_mainwindow_ui import Ui_SesionMainWindow
from ...servicios.gestor_inicio_sesion.gestor_sesion import GestorSesion


class UiInterfazSesion(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_SesionMainWindow()
        self.ui.setupUi(self)

        self.ui.iniciar_pushButton.clicked.connect(self.iniciar_sesion)

    @Slot()
    def iniciar_sesion(self):
        usuario = self.ui.usuario_lineEdit.text()
        contrasena = self.ui.contrasena_lineEdit.text()

        gestor_sesion = GestorSesion()
        gestor_sesion.IniciarSesion(usuario, contrasena)
