from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import Qt, Slot


from ..mainwindow_ui import Ui_MainWindow
from servicios.gestor_analisis_modulo.gestor_analisis import GestorAnalisis


class GestorGraficasAnalisisUI(object):
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.gestor_analisis = GestorAnalisis()
        # self.gestor_escritos = GestorEscritos()

        self.ui.Escritos_Guardar_pushButton.clicked.connect(self.analizar_escrito)

    @Slot()
    def analizar_escrito(self, texto):
        print("Generando analisis...")

        resultado = self.gestor_analisis.analizar_texto(texto)
        print(resultado)
        print("Analisis generado.")

        self.graficar_analisis(resultado)

    @Slot()
    def graficar_analisis(self, resultado):
        pass
