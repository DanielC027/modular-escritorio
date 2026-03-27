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
from .gestor_tree_widget import GestorTreeWidget


from ....servicios.gestor_analisis_modulo.gestor_analisis import GestorAnalisis
from ....servicios.gestor_escritos_modulo.gestor_escritos import GestorEscritos
from ....nucleo.hilo_modulo.trabajador_modulo import Trabajador

from ....servicios.gestor_escritos_modulo.gestor_escritos import GestorEscritos
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
        self.ui.Escritos_Guardar_pushButton.clicked.connect(self.guardar_escrito)
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
                self.guardar_escrito()

            dialogo = SelectorFecha()
            resultado = dialogo.exec()

            if resultado:
                fecha = dialogo.obtener_fecha().toString("yyyy-MM-dd")

                if not self.gestor_escritos.RevisarExisteFechaGuardada(
                    fecha, self.datos
                ):
                    self.gestor_treewidget.agregar_fecha_sin_guardar(fecha)

                    # Limpiar editor
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
            msgBox = QMessageBox()
            msgBox.critical(
                self.ui.centralwidget,
                "Error",
                "Error al crear escrito para editar.",
            )

    # ----- GUARDAR -----
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

            texto = self.ui.Escritos_Escrito_textEdit.toPlainText()

            if not texto.strip():
                QMessageBox.warning(
                    self.ui.centralwidget,
                    "Aviso",
                    "El escrito está vacío.",
                )
                return

            fecha = self.gestor_treewidget.fecha_actual

            resultado = self.gestor_escritos.GuardarEscrito(fecha, texto, self.datos)

            self.trabajad = Trabajador(self.gestor_analisis.analizar_texto, texto)
            self.trabajad.resultado.connect(self.graficar_analisis)
            self.trabajad.error.connect(self.error_proceso)
            self.trabajad.start()

            if resultado:
                self.gestor_treewidget.actualizar_fecha_guardada(fecha)

                QMessageBox.information(
                    self.ui.centralwidget,
                    "Guardado",
                    "Se ha guardado el escrito y se detectaron las emociones.",
                )
                self.ui.Escritos_Escrito_textEdit.setEnabled(False)
            else:
                QMessageBox.critical(
                    self.ui.centralwidget,
                    "Error",
                    "No fue posible crear el escrito o analizarlo.",
                )

        except Exception as ex:
            print(f"Error: {ex}")
            QMessageBox.critical(
                self.ui.centralwidget,
                "Error",
                "No fue posible crear el escrito o analizarlo.",
            )
            self.error_proceso()

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

        fecha = item.data(0, 0x0100)  # Qt.UserRole

        if not fecha:
            return

        if "*" in item.text(0):
            return  # aun no guardado

        #print("Abrir fecha:", fecha)
        contenido = self.gestor_escritos.LeerEscrito(fecha, self.datos)
        #print(contenido)
        if not contenido:
            QMessageBox.critical(
                self.ui.centralwidget,
                "Error",
                "No fue posible obtener el escrito.",
            )
            self.ui.Escritos_Escrito_textEdit.setDisabled(True)
        # Cargar escrito a text edit
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
