from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot, Signal

from .registro_mainwindow_ui import Ui_RegistroMainWindow
from ...servicios.gestor_inicio_sesion.gestor_sesion import GestorSesion


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

            if not usuario or not contrasena_1 or not contrasena_2:
                msgBox = QMessageBox()
                msgBox.setText("Datos incorrectos, intenta de nuevo.")
                msgBox.exec()
                return

            gestor_sesion = GestorSesion()
            gestor_sesion.RegistrarUsuario(usuario, contrasena_1, contrasena_2)

            msgBox = QMessageBox()
            msgBox.setText("Cuenta creada exitosamente.")
            msgBox.exec()

            self.registro_exitoso.emit()
        except Exception as ex:
            msgBox = QMessageBox()
            msgBox.setText(f"Error: {ex}")
            msgBox.exec()
