from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QMessageBox,
)
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import Qt, Slot


from ..mainwindow_ui import Ui_MainWindow
from servicios.gestor_analisis_modulo.gestor_analisis import GestorAnalisis
from nucleo.hilo_modulo.trabajador_modulo import Trabajador


class GestorEscritosUI(object):
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.gestor_analisis = GestorAnalisis()
        # self.gestor_escritos = GestorEscritos()

        self.ui.Escritos_Guardar_pushButton.clicked.connect(self.guardar_escrito)

    @Slot()
    def NuevoEscrito(self):
        print("Nuevo escrito")

    @Slot()
    def guardar_escrito(self):
        print("Guardar escrito")
        texto = self.ui.Escritos_Escrito_textEdit.toPlainText()
        print(texto)
        print("Generando analisis...")

        self.trabajad = Trabajador(self.gestor_analisis.analizar_texto, texto)
        self.trabajad.resultado.connect(self.graficar_analisis)
        self.trabajad.error.connect(self.error_proceso)
        self.trabajad.start()

    @Slot()
    def graficar_analisis(self, resultado):
        try:
            if "probabilidades" in resultado and "etiquetas" in resultado:
                probabilidades = resultado["probabilidades"]
                etiquetas = [
                    resultado["etiquetas"][i] for i in range(len(probabilidades))
                ]

                scene = QGraphicsScene()
                self.ui.Graficas_Grafica_graphicsView.setScene(scene)

                bar_width = 50
                spacing = 30
                max_height = 300  # altura máxima de la barra

                for i, prob in enumerate(probabilidades):
                    height = prob * max_height
                    rect = QGraphicsRectItem(
                        i * (bar_width + spacing),
                        max_height - height,
                        bar_width,
                        height,
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
                    value_text.setPos(
                        i * (bar_width + spacing), max_height - height - 20
                    )
                    value_text.setTextWidth(bar_width)
                    scene.addItem(value_text)

                scene.setSceneRect(
                    0, 0, len(probabilidades) * (bar_width + spacing), max_height + 50
                )

            print("Analisis generado.")
            QMessageBox.information(
                self.ui.centralwidget,
                "Información",
                "Se ha guardado el escrito y se detectaron las emociones.",
            )
        except Exception as ex:
            self.error_proceso()

    @Slot()
    def error_proceso(self):
        QMessageBox.critical(self.ui.centralwidget, "ERROR", "¡Ha ocurrido un error.!")
