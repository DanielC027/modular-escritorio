from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot, Signal
from .sesion_mainwindow_ui import Ui_SesionMainWindow
from ...servicios.gestor_inicio_sesion.gestor_sesion import GestorSesion


class UiInterfazSesion(QMainWindow):
    necesita_registro = Signal()
    inicio_satisfactorio = Signal(object)

    def __init__(self):
        super().__init__()

        self.ui = Ui_SesionMainWindow()
        self.ui.setupUi(self)

        self.ui.iniciar_pushButton.clicked.connect(self.iniciar_sesion)
        self.ui.registrarse_pushButton.clicked.connect(self.registrarse)

    @Slot()
    def iniciar_sesion(self):
        ESTADO = {"SIN_REGISTRO": 0, "AUTENTICADO": 1, "NO_AUTENTICADO": 2}

        if not GestorSesion().ExisteCuenta():
            print("revisado")
            self.necesita_registro.emit()
            return

        usuario = self.ui.usuario_lineEdit.text()
        contrasena = self.ui.contrasena_lineEdit.text()

        if not usuario or not contrasena:
            msgBox = QMessageBox()
            msgBox.critical(
                self.ui.centralwidget,
                "Error",
                "Usuario o Contraseña incorrecta, intenta de nuevo.",
            )
            return

        gestor_sesion = GestorSesion()
        respuesta = gestor_sesion.IniciarSesion(usuario, contrasena)
        # desde gestor sesion se envia el estado y la sal en caso de haber desencriptado
        if respuesta["estado"] == ESTADO["SIN_REGISTRO"]:
            self.necesita_registro.emit()
        elif respuesta["estado"] == ESTADO["AUTENTICADO"]:
            # datos para poder manipular escritos
            datos = {
                "usuario": usuario,
                "contrasena": contrasena,
                "sal": respuesta["sal"],
            }
            self.inicio_satisfactorio.emit(datos)
        elif respuesta["estado"] == ESTADO["NO_AUTENTICADO"]:
            msgBox = QMessageBox()
            msgBox.critical(
                self.ui.centralwidget,
                "Error",
                "Usuario o Contraseña incorrecta, intenta de nuevo.",
            )

    @Slot()
    def registrarse(self):
        if GestorSesion().ExisteCuenta():
            msgBox = QMessageBox()
            msgBox.setText("Cuenta ya creada.")
            msgBox.exec()
        else:
            self.necesita_registro.emit()
