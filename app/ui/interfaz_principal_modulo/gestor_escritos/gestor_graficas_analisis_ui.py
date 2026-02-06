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
        if "probabilidades" in resultado and "etiquetas" in resultado:
            probabilidades = resultado["probabilidades"]
            etiquetas = [resultado["etiquetas"][i] for i in range(len(probabilidades))]

            scene = QGraphicsScene()
            self.ui.Graficas_Grafica_graphicsView.setScene(scene)

            bar_width = 50
            spacing = 30
            max_height = 300  # altura máxima de la barra

            for i, prob in enumerate(probabilidades):
                height = prob * max_height
                rect = QGraphicsRectItem(
                    i * (bar_width + spacing), max_height - height, bar_width, height
                )
                rect.setBrush(QBrush(QColor("skyblue")))
                rect.setPen(Qt.NoPen)
                scene.addItem(rect)

                # Etiqueta debajo de la barra
                text = QGraphicsTextItem(etiquetas[i])
                text.setPos(i * (bar_width + spacing), max_height + 5)
                text.setTextWidth(bar_width)
                scene.addItem(text)

                # Valor encima de la barra
                value_text = QGraphicsTextItem(f"{prob:.3f}")
                value_text.setPos(i * (bar_width + spacing), max_height - height - 20)
                value_text.setTextWidth(bar_width)
                scene.addItem(value_text)

            scene.setSceneRect(
                0, 0, len(probabilidades) * (bar_width + spacing), max_height + 50
            )
