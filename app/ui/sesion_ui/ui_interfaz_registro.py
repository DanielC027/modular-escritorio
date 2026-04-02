from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot, Signal

from .registro_mainwindow_ui import Ui_RegistroMainWindow
from ...servicios.gestor_inicio_sesion.gestor_sesion import GestorSesion

import re

class UiInterfazRegistro(QMainWindow):
    registro_cancelado = Signal()
    registro_exitoso = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_RegistroMainWindow()
        self.ui.setupUi(self)

        self.ui.registrar_pushButton.clicked.connect(self.registrar_usuario)

    @Slot()
    def registrar_usuario(self):
        try:
            usuario = self.ui.usuario_lineEdit.text()
            contrasena_1 = self.ui.contrasena_1_lineEdit.text()
            contrasena_2 = self.ui.contrasena_2_lineEdit.text()

            patron_usuario = r'[a-zA-Z]+$'
            si_patron_usuario = re.match(patron_usuario,usuario)

            patron_password = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'
            si_patron_contrasena_1 = re.match(patron_password,contrasena_1)
            si_patron_contrasena_2 = re.match(patron_password,contrasena_2)

            #print(si_patron_usuario, " ",si_patron_contrasena_1, " ", si_patron_contrasena_2)

            if (
                not usuario
                or not contrasena_1
                or not contrasena_2
                or contrasena_1 == contrasena_2
                or not si_patron_usuario
                or not si_patron_contrasena_1
                or not si_patron_contrasena_2
            ):
                msgBox = QMessageBox()
                msgBox.critical(
                    self.ui.centralwidget,
                    "Error",
                    "Datos incorrectos, intenta de nuevo.",
                )
                return

            gestor_sesion = GestorSesion()
            gestor_sesion.RegistrarUsuario(usuario, contrasena_1, contrasena_2)

            msgBox = QMessageBox()
            msgBox.information(
                self.ui.centralwidget, "INFORMATION", "Cuenta creada exitosamente."
            )

            self.registro_exitoso.emit()
        except Exception as ex:
            msgBox = QMessageBox()
            msgBox.critical(self.ui.centralwidget, "Error", f"Error: {ex}")
