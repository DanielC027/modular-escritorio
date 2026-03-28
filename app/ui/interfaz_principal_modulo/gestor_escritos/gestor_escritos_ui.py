import torch
import json
from datetime import date
import time

from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QMessageBox,
)
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import Qt, Slot

from ..mainwindow_ui import Ui_MainWindow
from .gestor_tree_widget import GestorTreeWidget

from ....servicios.gestor_analisis_modulo.gestor_analisis import GestorAnalisis
from ....servicios.gestor_escritos_modulo.gestor_escritos import GestorEscritos
from ....nucleo.hilo_modulo.trabajador_modulo import Trabajador

from .selector_fecha_ui import SelectorFecha


class GestorEscritosUI:
    def __init__(self, ui: Ui_MainWindow, datos):
        self.ui = ui
        self.datos = datos

        self.gestor_analisis = GestorAnalisis()
        self.gestor_escritos = GestorEscritos()
        self.gestor_treewidget = GestorTreeWidget(self.ui)

        self.cargar_tree_widget_al_iniciar()

        # ----- CONEXIONES -----
        self.ui.Escritos_Nuevo_pushButton.clicked.connect(self.nuevo_escrito)
        self.ui.Escritos_Guardar_pushButton.clicked.connect(self.llamar_guardar)
        self.ui.Escritos_Eliminar_pushButton.clicked.connect(self.eliminar_escrito)

        self.ui.Escritos_Escritos_treeWidget.itemClicked.connect(self.on_item_click)

        self.ui.Escritos_Escrito_textEdit.setEnabled(False)

    def cargar_tree_widget_al_iniciar(self):
        lista_escritos = self.gestor_escritos.MostrarListaEscritos(self.datos)
        print(lista_escritos)
        self.gestor_treewidget.cargar_todas_las_fechas(lista_escritos)

    # ----- VALIDACIONES -----
    def validar_cambios_sin_guardar(self):
        if self.gestor_treewidget.sin_guardar:
            resp = QMessageBox.question(
                self.ui.centralwidget,
                "Cambios sin guardar",
                "Tienes cambios sin guardar. ¿Deseas continuar?",
                QMessageBox.Yes | QMessageBox.No,
            )
            return resp == QMessageBox.Yes
        return True

    # ----- NUEVO -----
    @Slot()
    def nuevo_escrito(self):
        try:
            if not self.validar_cambios_sin_guardar():
                return
            else:
                self.llamar_guardar()

            dialogo = SelectorFecha()
            resultado = dialogo.exec()

            if resultado:
                fecha = dialogo.obtener_fecha().toString("yyyy-MM-dd")

                if not self.gestor_escritos.RevisarExisteFechaGuardada(
                    fecha, self.datos
                ):
                    self.gestor_treewidget.agregar_fecha_sin_guardar(fecha)

                    self.ui.Escritos_Escrito_textEdit.clear()
                    self.ui.Escritos_Escrito_textEdit.setEnabled(True)
                else:
                    QMessageBox.critical(
                        self.ui.centralwidget,
                        "Error",
                        "Ya existe esa fecha guardada.",
                    )
        except Exception as ex:
            print(ex)
            QMessageBox.critical(
                self.ui.centralwidget,
                "Error",
                "Error al crear escrito para editar.",
            )

    # ----- GUARDAR -----
    def llamar_guardar(self):
        self.guardar_escrito()

    @Slot()
    def guardar_escrito(self):
        try:
            if not self.gestor_treewidget.fecha_actual:
                QMessageBox.warning(
                    self.ui.centralwidget,
                    "Aviso",
                    "No hay ningún escrito en edición.",
                )
                return

            # Desactivar botones
            self.ui.Escritos_Nuevo_pushButton.setEnabled(False)
            self.ui.Escritos_Guardar_pushButton.setEnabled(False)
            self.ui.Escritos_Eliminar_pushButton.setEnabled(False)

            texto = self.ui.Escritos_Escrito_textEdit.toPlainText()

            if not texto.strip():
                QMessageBox.warning(
                    self.ui.centralwidget,
                    "Aviso",
                    "El escrito está vacío.",
                )
                self.reactivar_botones()
                return

            fecha = self.gestor_treewidget.fecha_actual

            print("Guardando escrito...")
            resultado = self.gestor_escritos.GuardarEscrito(fecha, texto, self.datos)

            if not resultado:
                QMessageBox.critical(
                    self.ui.centralwidget,
                    "Error",
                    "No fue posible crear el escrito.",
                )
                self.reactivar_botones()
                return

            self.fecha_guardada_actual = fecha

            print("Iniciando análisis...")
            self.iniciar_analisis(texto)

        except Exception as ex:
            print(f"Error: {ex}")
            QMessageBox.critical(
                self.ui.centralwidget,
                "Error",
                f"No fue posible crear el escrito o analizarlo. {ex}",
            )
            self.reactivar_botones()

    def iniciar_analisis(self, texto):
        try:
            self.trabajador = Trabajador(self.gestor_analisis.analizar_texto, texto)
            self.trabajador.resultado.connect(self.analisis_completado)
            self.trabajador.error.connect(self.error_analisis)
            self.trabajador.finished.connect(self.trabajador.deleteLater)
            self.trabajador.start()
        except Exception as ex:
            print(ex)
            QMessageBox.critical(
                self.ui.centralwidget,
                "Error",
                f"No fue posible analizarlo. {ex}",
            )
            self.reactivar_botones()

    @Slot()
    def analisis_completado(self, resultado):
        try:
            print("Análisis completado")

            self.graficar_analisis(resultado)

            self.gestor_treewidget.actualizar_fecha_guardada(self.fecha_guardada_actual)

            QMessageBox.information(
                self.ui.centralwidget,
                "Guardado",
                "Se ha guardado el escrito y se detectaron las emociones.",
            )

            self.ui.Escritos_Escrito_textEdit.setEnabled(False)

        except Exception as ex:
            print(f"Error en análisis: {ex}")
            self.error_proceso()

        finally:
            self.reactivar_botones()

    @Slot()
    def error_analisis(self):
        QMessageBox.critical(
            self.ui.centralwidget,
            "Error",
            "¡Error durante el análisis!",
        )
        self.reactivar_botones()

    def reactivar_botones(self):
        self.ui.Escritos_Nuevo_pushButton.setEnabled(True)
        self.ui.Escritos_Guardar_pushButton.setEnabled(True)
        self.ui.Escritos_Eliminar_pushButton.setEnabled(True)

    # ----- ELIMINAR -----
    @Slot()
    def eliminar_escrito(self):
        if not self.validar_cambios_sin_guardar():
            return

        fecha = self.gestor_treewidget.obtener_fecha_seleccionada()

        if not fecha:
            QMessageBox.warning(
                self.ui.centralwidget,
                "Aviso",
                "Selecciona un escrito.",
            )
            return

        print("Eliminar:", fecha)
        self.gestor_escritos.MostrarListaEscritos(self.datos)
        self.ui.Escritos_Escrito_textEdit.setEnabled(False)

    # ----- ABRIR DESDE TREE -----
    def on_item_click(self, item, column):
        if not self.validar_cambios_sin_guardar():
            return

        fecha = item.data(0, 0x0100)

        if not fecha:
            return

        if "*" in item.text(0):
            return

        contenido = self.gestor_escritos.LeerEscrito(fecha, self.datos)

        if not contenido:
            QMessageBox.critical(
                self.ui.centralwidget,
                "Error",
                "No fue posible obtener el escrito.",
            )
            self.ui.Escritos_Escrito_textEdit.setDisabled(True)

        self.ui.Escritos_Escrito_textEdit.setPlainText(contenido)
        self.ui.Escritos_Escrito_textEdit.setEnabled(True)

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
                    "anger": "#e74c3c",
                    "disgust": "#27ae60",
                    "fear": "#8e44ad",
                    "joy": "#f1c40f",
                    "sadness": "#3498db",
                    "surprise": "#e67e22",
                    "others": "#95a5a6",
                }

                probabilidades = resultado["probabilidades"]
                etiquetas = [
                    resultado["etiquetas"][i] for i in range(len(probabilidades))
                ]

                if isinstance(probabilidades, torch.Tensor):
                    probs_lista = probabilidades.tolist()
                else:
                    probs_lista = list(probabilidades)

                scene = QGraphicsScene()
                self.ui.Graficas_Grafica_graphicsView.setScene(scene)

                bar_width = 50
                spacing = 30
                max_height = 300

                for i, prob in enumerate(probs_lista):
                    height = prob * max_height
                    etiqueta_en = str(etiquetas[i])

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

                    etiqueta_esp = TRADUCCION_ETIQUETAS.get(etiqueta_en, etiqueta_en)

                    text = QGraphicsTextItem(etiqueta_esp)
                    text.setPos(i * (bar_width + spacing), max_height + 5)
                    text.setTextWidth(bar_width)
                    text.setDefaultTextColor(QColor("white"))
                    scene.addItem(text)

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
                    "timestamp": int(time.time()),
                    "valores": {
                        "probabilidades": probs_lista,
                        "etiquetas": [
                            TRADUCCION_ETIQUETAS.get(e, e) for e in etiquetas
                        ],
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
