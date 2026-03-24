from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt


class GestorTreeWidget:
    def __init__(self, ui):
        self.ui = ui
        self.tree = self.ui.Escritos_Escritos_treeWidget

        self.items_por_fecha = {}  # "2026-02-05" -> item
        self.fecha_actual = None
        self.sin_guardar = False

        self.tree.expandAll()  # Quitar al final

    # ----- UTILIDADES INTERNAS -----
    def _obtener_o_crear_item(self, parent, texto):
        for i in range(parent.childCount()):
            if parent.child(i).text(0) == texto:
                return parent.child(i)

        item = QTreeWidgetItem()
        item.setText(0, texto)
        parent.addChild(item)
        return item

    def _obtener_o_crear_anio(self, anio):
        for i in range(self.tree.topLevelItemCount()):
            item = self.tree.topLevelItem(i)
            if item.text(0) == anio:
                return item

        item = QTreeWidgetItem()
        item.setText(0, anio)
        self.tree.addTopLevelItem(item)
        return item

    # ----- FUNCIONES PRINCIPALES -----
    def agregar_fecha_sin_guardar(self, fecha):
        # fecha: "2026-02-05"
        anio, mes, dia = fecha.split("-")

        anio_item = self._obtener_o_crear_anio(anio)
        mes_item = self._obtener_o_crear_item(anio_item, mes)

        texto = f"{dia}/{mes}/{anio} *"

        dia_item = QTreeWidgetItem()
        dia_item.setText(0, texto)

        # Guardar fecha real
        dia_item.setData(0, Qt.UserRole, fecha)

        # Color amarillo
        dia_item.setForeground(0, QColor("yellow"))

        mes_item.addChild(dia_item)

        self.items_por_fecha[fecha] = dia_item
        self.fecha_actual = fecha
        self.sin_guardar = True

        self.tree.expandAll()

    def actualizar_fecha_guardada(self, fecha):
        item = self.items_por_fecha.get(fecha)

        if not item:
            return

        texto = item.text(0).replace(" *", "")
        item.setText(0, texto)

        # Color normal
        item.setForeground(0, QColor("white"))

        self.sin_guardar = False

    def obtener_fecha_seleccionada(self):
        item = self.tree.currentItem()
        if not item:
            return None

        return item.data(0, Qt.UserRole)

    def cargar_todas_las_fechas(self, lista_fechas):
        """
        lista_fechas = ["2026-02-05", "2026-02-06", ...]
        """
        self.tree.clear()
        self.items_por_fecha.clear()

        for fecha in lista_fechas:
            anio, mes, dia = fecha.split("-")

            anio_item = self._obtener_o_crear_anio(anio)
            mes_item = self._obtener_o_crear_item(anio_item, mes)

            texto = f"{dia}/{mes}/{anio}"

            dia_item = QTreeWidgetItem()
            dia_item.setText(0, texto)
            dia_item.setData(0, Qt.UserRole, fecha)

            mes_item.addChild(dia_item)

            self.items_por_fecha[fecha] = dia_item

        self.tree.expandAll()  # Quitar al final
