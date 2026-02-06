from PySide6.QtWidgets import QApplication
from ui.interfaz_principal_modulo.ui_interfaz_principal import UiInterfazPrincipal
import sys

from bd import init_db

init_db()

app = QApplication(sys.argv)

window = UiInterfazPrincipal()

window.show()


sys.exit(app.exec())
