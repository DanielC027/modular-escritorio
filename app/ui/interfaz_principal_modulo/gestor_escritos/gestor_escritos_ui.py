import json
from datetime import date
import base64

from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QMessageBox,
)
from PySide6.QtGui import QBrush, QColor
from PySide6.QtCore import Qt, Slot

from ..mainwindow_ui import Ui_MainWindow
from .gestor_graficas_analisis_ui import GestorGraficasAnalisisUI
from .gestor_tree_widget import GestorTreeWidget

from ....servicios.gestor_analisis_modulo.gestor_analisis import GestorAnalisis

from ....servicios.gestor_escritos_modulo.gestor_escritos import GestorEscritos
from ....nucleo.hilo_modulo.trabajador_modulo import Trabajador

from .selector_fecha_ui import SelectorFecha


class GestorEscritosUI:
    def __init__(self, ui: Ui_MainWindow, datos):
        self.ui = ui
        self.datos = datos

        self.gestor_analisis_ui = GestorGraficasAnalisisUI(self.ui)

        self.gestor_analisis = GestorAnalisis()
        self.gestor_escritos = GestorEscritos()
        self.gestor_treewidget = GestorTreeWidget(self.ui)

        self.cargar_tree_widget_al_iniciar()

        self.contenido_original = ""

        self.ui.Escritos_Escrito_textEdit.textChanged.connect(self.detectar_cambios)
        # ----- CONEXIONES -----
        self.ui.Escritos_Nuevo_pushButton.clicked.connect(self.nuevo_escrito)
        self.ui.Escritos_Guardar_pushButton.clicked.connect(self.llamar_guardar)
        self.ui.Escritos_Eliminar_pushButton.clicked.connect(self.eliminar_escrito)

        self.ui.Escritos_Escritos_treeWidget.itemClicked.connect(self.on_item_click)

        self.ui.Escritos_Escrito_textEdit.setEnabled(False)

        self.ui.Graficas_Fecha_dateEdit.dateChanged.connect(
            self.graficar_seccion_graficas
        )

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

    def detectar_cambios(self):
        if not self.gestor_treewidget.fecha_actual:
            return

        texto_actual = self.ui.Escritos_Escrito_textEdit.toPlainText()

        if texto_actual != self.contenido_original:
            self.gestor_treewidget.marcar_como_modificado(
                self.gestor_treewidget.fecha_actual
            )
        else:
            self.gestor_treewidget.limpiar_modificado(
                self.gestor_treewidget.fecha_actual
            )

    # ----- NUEVO -----
    @Slot()
    def nuevo_escrito(self):
        try:
            if self.validar_cambios_sin_guardar():
                self.guardar_escrito()
            else:
                return

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

            existe = self.gestor_escritos.RevisarExisteFechaGuardada(fecha, self.datos)

            if existe:
                resultado = self.gestor_escritos.ActualizarEscrito(
                    fecha, texto, self.datos
                )
            else:
                resultado = self.gestor_escritos.GuardarEscrito(
                    fecha, texto, self.datos
                )

            if not resultado:
                QMessageBox.critical(
                    self.ui.centralwidget,
                    "Error",
                    "No fue posible guardar el escrito.",
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

            id_escrito = self.gestor_escritos.ObtenerIDEscrito(
                self.fecha_guardada_actual, self.datos
            )
            self.gestor_treewidget.actualizar_fecha_guardada(self.fecha_guardada_actual)
            print(resultado)
            self.graficar_analisis(resultado, self.fecha_guardada_actual, id_escrito)

            QMessageBox.information(
                self.ui.centralwidget,
                "Guardado",
                "Se ha guardado el escrito y se detectaron las emociones.",
            )

            self.ui.Escritos_Escrito_textEdit.setEnabled(False)

            self.contenido_original = self.ui.Escritos_Escrito_textEdit.toPlainText()
            self.gestor_treewidget.limpiar_modificado(self.fecha_guardada_actual)
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

        resultado = self.gestor_escritos.EliminarEscrito(fecha, self.datos)
        if resultado:
            QMessageBox.information(
                self.ui.centralwidget,
                "Informacion",
                "Escrito eliminado.",
            )
        else:
            QMessageBox.critical(
                self.ui.centralwidget,
                "Error",
                "No fue posible eliminar.",
            )
        self.cargar_tree_widget_al_iniciar()
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

        contenido = self.gestor_escritos.LeerEscrito(fecha, self.datos)

        if not contenido:
            QMessageBox.critical(
                self.ui.centralwidget,
                "Error",
                "No fue posible obtener el escrito.",
            )
            self.ui.Escritos_Escrito_textEdit.setDisabled(True)
            return

        self.gestor_treewidget.fecha_actual = fecha

        self.ui.Escritos_Escrito_textEdit.blockSignals(True)
        self.ui.Escritos_Escrito_textEdit.setPlainText(contenido)
        self.ui.Escritos_Escrito_textEdit.blockSignals(False)

        self.contenido_original = contenido
        self.gestor_treewidget.sin_guardar = False

        self.ui.Escritos_Escrito_textEdit.setEnabled(True)

    @Slot()
    def graficar_analisis(self, resultado, fecha, id_escrito):
        try:
            huella_digital = self.gestor_escritos.GenerarHuellaDigital(self.datos)

            # DATOS DIA
            resultado_dia = self.gestor_analisis.obtener_analisis_dia(
                fecha, huella_digital
            )
            """etiquetas_dia = [dato[0] for dato in resultado_dia]
            probabilidades_dia = [dato[1] for dato in resultado_dia]
            datos_dia = {
                "probabilidades": probabilidades_dia,
                "etiquetas": {
                    index: etiqueta for index, etiqueta in enumerate(etiquetas_dia)
                },
            }"""
            datos_dia = resultado
            # DATOS SEMANA
            resultado_semana = self.gestor_analisis.obtener_analisis_semana(
                fecha, huella_digital
            )
            etiquetas_semana = [anio[1] for anio in resultado_semana]
            probabilidades_semana = [anio[2] for anio in resultado_semana]
            datos_semana = {
                "probabilidades": probabilidades_semana,
                "etiquetas": {
                    index: etiqueta for index, etiqueta in enumerate(etiquetas_semana)
                },
            }

            # DATOS MES
            resultado_mes = self.gestor_analisis.obtener_analisis_mes(
                fecha, huella_digital
            )
            etiquetas_mes = [anio[1] for anio in resultado_mes]
            probabilidades_mes = [anio[2] for anio in resultado_mes]
            datos_mes = {
                "probabilidades": probabilidades_mes,
                "etiquetas": {
                    index: etiqueta for index, etiqueta in enumerate(etiquetas_mes)
                },
            }

            # DATOS ANIO
            resultado_anio = self.gestor_analisis.obtener_analisis_anio(
                fecha, huella_digital
            )
            etiquetas_anio = [anio[1] for anio in resultado_anio]
            probabilidades_anio = [anio[2] for anio in resultado_anio]
            datos_anio = {
                "probabilidades": probabilidades_anio,
                "etiquetas": {
                    index: etiqueta for index, etiqueta in enumerate(etiquetas_anio)
                },
            }

            # print(datos_anio)
            huella_digital_decode = huella_digital.decode("utf-8")
            # print(huella_digital_decode)

            self.gestor_analisis_ui.graficar_dia(
                huella_digital_decode, datos_dia, fecha, id_escrito
            )
            self.gestor_analisis_ui.graficar_semana(
                huella_digital_decode, datos_semana, fecha, id_escrito
            )
            self.gestor_analisis_ui.graficar_mes(
                huella_digital_decode, datos_mes, fecha, id_escrito
            )
            self.gestor_analisis_ui.graficar_anio(
                huella_digital_decode, datos_anio, fecha, id_escrito
            )
        except Exception as ex:
            print(ex)
            self.error_proceso()
            # open<codigoasscii>

            """ Estoy escribiendo esto el 10 de abril y estoy en una fiesta con la familia de mi novio precioso hermoso chulo. El tiene que estar haciendo su tarea porque dentro de un mes (si Dios quiere) va a concluir una gran etapa de su vida, y es requisito que termine con esto, así que quiero que quede registrado aquí este gran día. Amén. Pd: Loa mo mucho  y es el amor de mi vida, y estoy muy orgullosa de el.  """

    @Slot()
    def graficar_seccion_graficas(self):
        try:
            fecha = self.ui.Graficas_Fecha_dateEdit.date().toString("yyyy-MM-dd")

            id_escrito = self.gestor_escritos.ObtenerIDEscrito(fecha, self.datos)

            huella_digital = self.gestor_escritos.GenerarHuellaDigital(self.datos)

            # DATOS DIA
            resultado_dia = self.gestor_analisis.obtener_analisis_dia(
                fecha, huella_digital
            )
            etiquetas_dia = [dato[0] for dato in resultado_dia]
            probabilidades_dia = [dato[1] for dato in resultado_dia]
            datos_dia = {
                "probabilidades": probabilidades_dia,
                "etiquetas": {
                    index: etiqueta for index, etiqueta in enumerate(etiquetas_dia)
                },
            }

            # DATOS SEMANA
            resultado_semana = self.gestor_analisis.obtener_analisis_semana(
                fecha, huella_digital
            )
            etiquetas_semana = [anio[1] for anio in resultado_semana]
            probabilidades_semana = [anio[2] for anio in resultado_semana]
            datos_semana = {
                "probabilidades": probabilidades_semana,
                "etiquetas": {
                    index: etiqueta for index, etiqueta in enumerate(etiquetas_semana)
                },
            }

            # DATOS MES
            resultado_mes = self.gestor_analisis.obtener_analisis_mes(
                fecha, huella_digital
            )
            etiquetas_mes = [anio[1] for anio in resultado_mes]
            probabilidades_mes = [anio[2] for anio in resultado_mes]
            datos_mes = {
                "probabilidades": probabilidades_mes,
                "etiquetas": {
                    index: etiqueta for index, etiqueta in enumerate(etiquetas_mes)
                },
            }

            # DATOS ANIO
            resultado_anio = self.gestor_analisis.obtener_analisis_anio(
                fecha, huella_digital
            )
            etiquetas_anio = [anio[1] for anio in resultado_anio]
            probabilidades_anio = [anio[2] for anio in resultado_anio]
            datos_anio = {
                "probabilidades": probabilidades_anio,
                "etiquetas": {
                    index: etiqueta for index, etiqueta in enumerate(etiquetas_anio)
                },
            }

            print(datos_anio)
            huella_digital_decode = huella_digital.decode("utf-8")
            # print(huella_digital_decode)

            self.gestor_analisis_ui.graficar_dia(
                huella_digital_decode, datos_dia, fecha, id_escrito
            )
            self.gestor_analisis_ui.graficar_semana(
                huella_digital_decode, datos_semana, fecha, id_escrito
            )
            self.gestor_analisis_ui.graficar_mes(
                huella_digital_decode, datos_mes, fecha, id_escrito
            )
            self.gestor_analisis_ui.graficar_anio(
                huella_digital_decode, datos_anio, fecha, id_escrito
            )
        except Exception as ex:
            print(ex)
            self.error_proceso()
            # open<codigoasscii>

    @Slot()
    def error_proceso(self):
        QMessageBox.critical(
            self.ui.centralwidget,
            "ERROR",
            "¡Ha ocurrido un error durante la graficación!",
        )
