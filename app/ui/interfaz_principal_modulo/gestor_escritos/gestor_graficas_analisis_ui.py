from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import Qt, Slot

import unicodedata

import time
import torch

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

import pyqtgraph as pg
from PySide6.QtWidgets import QVBoxLayout


class GestorGraficasAnalisisUI(object):
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.gestor_analisis = GestorAnalisis()

    def graficar_dia(self, resultado, fecha, id_escrito):
        self.graficar_analisis_qt(
            resultado, self.ui.dia_graphic_widget, fecha, id_escrito, True
        )

    def graficar_semana(self, resultado, fecha, id_escrito):
        self.graficar_analisis_qt(
            resultado, self.ui.semana_graphic_widget, fecha, id_escrito, False
        )

    def graficar_mes(self, resultado, fecha, id_escrito):
        self.graficar_analisis_qt(
            resultado, self.ui.mes_graphic_widget, fecha, id_escrito, False
        )

    def graficar_anio(self, resultado, fecha, id_escrito):
        self.graficar_analisis_qt(
            resultado, self.ui.anio_graphic_widget, fecha, id_escrito, False
        )

    def graficar_analisis_qt(
        self, resultado, graphic_widget, fecha, id_escrito, guardar
    ):
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
                    "anger": "#e74c3c",
                    "disgust": "#27ae60",
                    "fear": "#8e44ad",
                    "joy": "#f1c40f",
                    "sadness": "#3498db",
                    "surprise": "#e67e22",
                    "others": "#95a5a6",
                }
                print(resultado)
                probabilidades = resultado["probabilidades"]
                etiquetas = [
                    resultado["etiquetas"][i] for i in range(len(probabilidades))
                ]

                # convertir tensor si aplica
                if isinstance(probabilidades, torch.Tensor):
                    probs_lista = probabilidades.tolist()
                else:
                    probs_lista = list(probabilidades)

                # limpiar widget anterior
                if graphic_widget.layout() is not None:
                    while graphic_widget.layout().count():
                        item = graphic_widget.layout().takeAt(0)
                        widget = item.widget()
                        if widget is not None:
                            widget.deleteLater()
                else:
                    graphic_widget.setLayout(QVBoxLayout())

                layout = graphic_widget.layout()

                # crear gráfica
                plot = pg.PlotWidget()
                layout.addWidget(plot)

                x = list(range(len(probs_lista)))

                brushes_color = []
                etiquetas_es = []

                if etiquetas[0] == "otros":
                    TRADUCCION_ETIQUETAS_ESP = {
                        v: k for k, v in TRADUCCION_ETIQUETAS.items()
                    }
                    for e in etiquetas:
                        e = self.limpiar_etiqueta(e)
                        nombre_ing = TRADUCCION_ETIQUETAS_ESP.get(e, "joy")
                        color = COLORES_EMOCIONES.get(nombre_ing, "#7f8c8d")
                        # print(color)
                        brushes_color.append(pg.mkBrush(QColor(color)))

                        etiquetas_es.append(e)
                else:
                    for e in etiquetas:
                        e = self.limpiar_etiqueta(e)
                        color = COLORES_EMOCIONES.get(e, "#7f8c8d")
                        # print(color)
                        brushes_color.append(pg.mkBrush(QColor(color)))

                        etiquetas_es.append(TRADUCCION_ETIQUETAS.get(e, e))

                # print(brushes_color)
                # barras
                bg = pg.BarGraphItem(
                    x=x, height=probs_lista, width=0.6, brushes=brushes_color
                )

                plot.addItem(bg)

                # etiquetas eje X
                axis = plot.getAxis("bottom")
                axis.setTextPen("white")
                axis.setTicks([list(zip(x, etiquetas_es))])

                axis_left = plot.getAxis("left")
                axis_left.setTextPen("white")

                # AGREGAR PORCENTAJES ARRIBA DE CADA BARRA
                for i, prob in enumerate(probs_lista):
                    porcentaje = f"{prob * 100:.1f}%"

                    texto = pg.TextItem(
                        text=porcentaje,
                        anchor=(0.5, 1),  # centrado arriba
                        color="white",
                    )

                    texto.setPos(i, prob)
                    plot.addItem(texto)

                plot.setYRange(0, 1)
                plot.setTitle("Análisis de emociones", color="white")
                plot.setLabel("left", "Probabilidad", color="white")
                plot.setLabel("bottom", "Emoción", color="white")
                plot.setBackground(QColor("#2a2a40"))

            mensaje = {
                "tipo": "analisis_emociones",
                "fecha": fecha,
                "id_escrito": id_escrito,
                "timestamp": int(time.time()),
                "valores": {
                    "probabilidades": probs_lista,
                    "etiquetas": [TRADUCCION_ETIQUETAS.get(e, e) for e in etiquetas],
                },
            }
            if guardar:
                self.guardar_analisis_bd(mensaje)
                self.gestor_analisis.enviar_datos_ws(mensaje)

        except Exception as ex:
            print("Error graficando:", ex)
            self.error_proceso()

    def guardar_analisis_bd(self, analisis):
        try:
            # print(analisis)
            self.gestor_analisis.guardar_analisis(analisis)
        except Exception as ex:
            print(ex)
            self.error_proceso()

    @Slot()
    def error_proceso(self):
        QMessageBox.critical(
            self.ui.centralwidget,
            "ERROR",
            "¡Ha ocurrido un error durante el análisis o el guardado!",
        )

    def limpiar_etiqueta(self, e):
        e = str(e).lower().strip()
        e = unicodedata.normalize("NFKD", e)
        return e
