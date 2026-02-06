from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from .mainwindow_ui import Ui_MainWindow

from .gestor_escritos.gestor_escritos_ui import GestorEscritosUI


class UiInterfazPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.gestorEscritos = GestorEscritosUI(self.ui, GestorAnalisis, GestorEscritos)
        self.gestorEscritos = GestorEscritosUI(self.ui)
