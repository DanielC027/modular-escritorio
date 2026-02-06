from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import Qt, Slot


from ..mainwindow_ui import Ui_MainWindow
from .gestor_graficas_analisis_ui import GestorGraficasAnalisisUI


class GestorEscritosUI(object):
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.gestor_analisis = GestorGraficasAnalisisUI(ui)

        self.ui.Escritos_Guardar_pushButton.clicked.connect(self.guardar_escrito)

    @Slot()
    def NuevoEscrito(self):
        print("Nuevo escrito")

    @Slot()
    def guardar_escrito(self):
        print("Guardar escrito")
        texto = self.ui.Escritos_Escrito_textEdit.toPlainText()
