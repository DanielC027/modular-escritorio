import asyncio
import torch
import json
import threading
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
from ....servicios.gestor_conexion_websocket.gestor_conexion_ws import BackendWSService
from ....nucleo.hilo_modulo.trabajador_modulo import Trabajador


class GestorEscritosUI:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.gestor_analisis = GestorAnalisis()

        # Crear loop de asyncio en un hilo separado
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self._run_loop, args=(self.loop,), daemon=True).start()

        # Inicializar WebSocket en el loop
        asyncio.run_coroutine_threadsafe(self._conectar_ws(), self.loop)

        # Conectar botones
        self.ui.Escritos_Guardar_pushButton.clicked.connect(self.guardar_escrito)

    def _run_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def _conectar_ws(self):
        self.backend_ws = BackendWSService("ws://127.0.0.1:8000/ws")
        try:
            await self.backend_ws.conectar()
            print("Conectado al backend WebSocket")
        except Exception as e:
            print("Error al conectar WS:", e)

    @Slot()
    def NuevoEscrito(self):
        print("Nuevo escrito")

    @Slot()
    def guardar_escrito(self):
        texto = self.ui.Escritos_Escrito_textEdit.toPlainText()
        print("Texto ingresado:", texto)
        print("Generando análisis...")

        # Ejecutar análisis en QThread
        self.trabajad = Trabajador(self.gestor_analisis.analizar_texto, texto)
        self.trabajad.resultado.connect(self.graficar_analisis)
        self.trabajad.error.connect(self.error_proceso)
        self.trabajad.start()

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
                    rect = QGraphicsRectItem(
                        i * (bar_width + spacing),
                        max_height - height,
                        bar_width,
                        height,
                    )
                    rect.setBrush(QBrush(QColor("skyblue")))
                    rect.setPen(Qt.NoPen)
                    scene.addItem(rect)

                    # Etiqueta debajo
                    etiqueta_en = str(etiquetas[i])
                    etiqueta_esp = TRADUCCION_ETIQUETAS.get(etiqueta_en, etiqueta_en)
                    text = QGraphicsTextItem(etiqueta_esp)
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
                    0, 0, len(probs_lista) * (bar_width + spacing), max_height + 50
                )

            QMessageBox.information(
                self.ui.centralwidget,
                "Información",
                "Se ha guardado el escrito y se detectaron las emociones.",
            )

            # Preparar mensaje JSON para el backend
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

            print("mensaje: ", mensaje)

            # Enviar al backend sin bloquear la UI
            async def enviar_ws():
                try:
                    await self.backend_ws.enviar(mensaje)
                    print("Mensaje enviado al backend")
                except Exception as e:
                    print("Error enviando WS:", e)

            # Ejecutar en el loop del hilo
            asyncio.run_coroutine_threadsafe(enviar_ws(), self.loop)

        except Exception as ex:
            print("Error graficando análisis:", ex)
            self.error_proceso()

    @Slot()
    def error_proceso(self):
        QMessageBox.critical(
            self.ui.centralwidget, "ERROR", "¡Ha ocurrido un error durante el análisis!"
        )
