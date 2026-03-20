import torch
import json
import asyncio
from datetime import date

from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QMessageBox,
)
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import Qt, Slot

from ..mainwindow_ui import Ui_MainWindow

from ....servicios.gestor_analisis_modulo.gestor_analisis import GestorAnalisis
from ....servicios.gestor_escritos_modulo.gestor_escritos import GestorEscritos
from ....nucleo.hilo_modulo.trabajador_modulo import Trabajador


class GestorEscritosUI:
    def __init__(self, ui: Ui_MainWindow, datos):
        self.ui = ui
        self.gestor_analisis = GestorAnalisis()
        self.gestor_escritos = GestorEscritos()

        self.datos = datos
        # Conectar botones
        self.ui.Escritos_Guardar_pushButton.clicked.connect(self.guardar_escrito)

    @Slot()
    def NuevoEscrito(self):
        print("Nuevo escrito")

    @Slot()
    def guardar_escrito(self):
        try:
            texto = self.ui.Escritos_Escrito_textEdit.toPlainText()
            print("Texto ingresado:", texto)
            print("Generando análisis...")

            # Ejecutar análisis en QThread
            self.gestor_escritos.GuardarEscrito(date.today(), texto, self.datos)

            self.trabajad = Trabajador(self.gestor_analisis.analizar_texto, texto)
            self.trabajad.resultado.connect(self.graficar_analisis)
            self.trabajad.error.connect(self.error_proceso)
            self.trabajad.start()

            QMessageBox.information(
                self.ui.centralwidget,
                "Información",
                "Se ha guardado el escrito y se detectaron las emociones.",
            )
        except Exception as ex:
            print(f"Error: {ex}")
            self.error_proceso()

    @Slot()
    def graficar_analisis(self, resultado):
        try:
            if "probabilidades" in resultado and "etiquetas" in resultado:
                TRADUCCION_ETIQUETAS = {
                    "anger": "enojo",
                    "disgust": "asco",
                    "fear": "miedo",
                    "joy": "alegría",
                    "sadness": "tristeza",
                    "surprise": "sorpresa",
                    "others": "otros",
                }
                COLORES_EMOCIONES = {
                    "anger": "#e74c3c",  # rojo
                    "disgust": "#27ae60",  # verde
                    "fear": "#8e44ad",  # morado
                    "joy": "#f1c40f",  # amarillo
                    "sadness": "#3498db",  # azul
                    "surprise": "#e67e22",  # naranja
                    "others": "#95a5a6",  # gris
                }
                probabilidades = resultado["probabilidades"]
                etiquetas = [
                    resultado["etiquetas"][i] for i in range(len(probabilidades))
                ]

                # Convertir tensor a lista de floats
                if isinstance(probabilidades, torch.Tensor):
                    probs_lista = probabilidades.tolist()
                else:
                    probs_lista = list(probabilidades)

                # Graficar barras
                scene = QGraphicsScene()
                self.ui.Graficas_Grafica_graphicsView.setScene(scene)

                bar_width = 50
                spacing = 30
                max_height = 300  # altura máxima de la barra

                for i, prob in enumerate(probs_lista):
                    height = prob * max_height
                    etiqueta_en = str(etiquetas[i])

                    # Color según emoción
                    color_barra = COLORES_EMOCIONES.get(etiqueta_en, "#7f8c8d")

                    rect = QGraphicsRectItem(
                        i * (bar_width + spacing),
                        max_height - height,
                        bar_width,
                        height,
                    )
                    rect.setBrush(QBrush(QColor(color_barra)))
                    rect.setPen(Qt.NoPen)
                    scene.addItem(rect)

                    # Traducción
                    etiqueta_esp = TRADUCCION_ETIQUETAS.get(etiqueta_en, etiqueta_en)

                    # Texto etiqueta (BLANCO)
                    text = QGraphicsTextItem(etiqueta_esp)
                    text.setPos(i * (bar_width + spacing), max_height + 5)
                    text.setTextWidth(bar_width)
                    text.setDefaultTextColor(QColor("white"))
                    scene.addItem(text)

                    # Valor encima (BLANCO)
                    value_text = QGraphicsTextItem(f"{prob:.3f}")
                    value_text.setPos(
                        i * (bar_width + spacing), max_height - height - 20
                    )
                    value_text.setTextWidth(bar_width)
                    value_text.setDefaultTextColor(QColor("white"))
                    scene.addItem(value_text)

                scene.setSceneRect(
                    0, 0, len(probs_lista) * (bar_width + spacing), max_height + 50
                )

            mensaje = {
                "tipo": "analisis_emociones",
                "timestamp": int(
                    asyncio.get_event_loop().time()
                ),  # usar asyncio solo en hilo
                "valores": {
                    "probabilidades": probs_lista,
                    "etiquetas": [TRADUCCION_ETIQUETAS.get(e, e) for e in etiquetas],
                },
            }

            self.gestor_analisis.enviar_datos_ws(mensaje)
        except Exception as ex:
            print("Error graficando análisis:", ex)
            self.error_proceso()

    @Slot()
    def error_proceso(self):
        QMessageBox.critical(
            self.ui.centralwidget,
            "ERROR",
            "¡Ha ocurrido un error durante el análisis o el guardado!",
        )
