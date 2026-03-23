from ..mainwindow_ui import Ui_MainWindow

from PySide6.QtWidgets import QTreeWidgetItem


class GestorTreeWidget:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.ui.Escritos_Escritos_treeWidget.expandAll()
        item = QTreeWidgetItem()
        item.setText(0, "2027")

        self.ui.Escritos_Escritos_treeWidget.addTopLevelItem(item)

    def agregar_fecha_sin_guardar(self, fecha):
        print("Agregar fecha sin guardar con * y color amarillo")

    def actaulizar_fecha_guardada(self, fecha):
        print("Actualizar fecha y quitar * y quitar color amarillo")

    def obtener_fecha_seleccionada(self):
        print("Regresar fecha seleccionada")

    def cargar_todas_las_fechas(self):
        print("Cargar todas las fechas")
