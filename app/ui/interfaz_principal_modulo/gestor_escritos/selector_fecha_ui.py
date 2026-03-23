from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QCalendarWidget,
    QPushButton,
    QHBoxLayout,
)
from PySide6.QtCore import QDate


class SelectorFecha(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar fecha")
        self.fecha_seleccionada = None

        layout = QVBoxLayout()

        self.calendario = QCalendarWidget()
        layout.addWidget(self.calendario)

        botones_layout = QHBoxLayout()

        btn_aceptar = QPushButton("Aceptar")
        btn_cancelar = QPushButton("Cancelar")

        btn_aceptar.clicked.connect(self.aceptar)
        btn_cancelar.clicked.connect(self.reject)

        botones_layout.addWidget(btn_aceptar)
        botones_layout.addWidget(btn_cancelar)

        layout.addLayout(botones_layout)
        self.setStyleSheet(
            "/* Fondo general */\n"
            "QWidget {\n"
            "    background-color: #1e1e2f;\n"
            "    color: #f0f0f0;\n"
            '    font-family: "Segoe UI", Arial, sans-serif;\n'
            "    font-size: 14px;\n"
            "}\n"
            "\n"
            "/* Botones */\n"
            "QPushButton {\n"
            "    background-color: #3a3f5a;\n"
            "    border: none;\n"
            "    border-radius: 8px;\n"
            "    padding: 6px 12px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #50577a;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #2c3147;\n"
            "}\n"
            "\n"
            "/* Inputs */\n"
            "QLineEdit, QTextEdit, QPlainTextEdit {\n"
            "    background-color: #2a2f45;\n"
            "    border: 1px solid #3f4662;\n"
            "    border-radius: 6px;\n"
            "    padding: 6px;\n"
            "}\n"
            "\n"
            "/* Labels */\n"
            "QLabel {\n"
            "    color: #e0e0e0;\n"
            "}\n"
            "\n"
            "/* ComboBox */\n"
            "QComboBox {\n"
            "    background-color: #2a2f45;\n"
            "    border: 1px solid #3f4662;\n"
            "    border-radius: 6px;\n"
            "    padding: 5px;\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "/* Scrollbar */\n"
            "QScrollBar:vertical {\n"
            "    backg"
            "round: #1e1e2f;\n"
            "    width: 10px;\n"
            "    margin: 2px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "    background: #3a3f5a;\n"
            "    border-radius: 5px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical:hover {\n"
            "    background: #50577a;\n"
            "}\n"
            "\n"
            "/* CheckBox */\n"
            "QCheckBox {\n"
            "    spacing: 6px;\n"
            "}\n"
            "\n"
            "QCheckBox::indicator {\n"
            "    width: 14px;\n"
            "    height: 14px;\n"
            "}\n"
            "\n"
            "QCheckBox::indicator:checked {\n"
            "    background-color: #6c8cff;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "/* Tabs */\n"
            "QTabWidget::pane {\n"
            "    border: 1px solid #3f4662;\n"
            "}\n"
            "\n"
            "QTabBar::tab {\n"
            "    background: #2a2f45;\n"
            "    padding: 8px;\n"
            "    border-top-left-radius: 6px;\n"
            "    border-top-right-radius: 6px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:selected {\n"
            "    background: #3a3f5a;\n"
            "}\n"
            "\n"
            "/* Tooltips */\n"
            "QToolTip {\n"
            "    background-color: #3a3f5a;\n"
            "    color: #ffffff;\n"
            "    border: 1px solid #6c8cff;\n"
            "}\n"
            "QCalendarWidget QAbstractItemView {\n"
            "    background-color: #2a2f45;\n"
            "    color: #f0f0f0;\n"
            "    selection-background-color: #6c8cff;\n"
            "    selection-color: #ffffff;\n"
            "}\n"
            "QCalendarWidget QAbstractItemView:enabled {\n"
            "    selection-background-color: #6c8cff;\n"
            "    selection-color: #ffffff;\n"
            "}\n"
            "QCalendarWidget QAbstractItemView::item:selected {\n"
            "    background-color: #6c8cff;\n"
            "    color: #ffffff;\n"
            "}\n"
            "QCalendarWidget QAbstractItemView::item:hover {\n"
            "    background-color: #50577a;\n"
            "}\n"
        )
        self.setLayout(layout)

    def aceptar(self):
        self.fecha_seleccionada = self.calendario.selectedDate()
        self.accept()

    def obtener_fecha(self):
        return self.fecha_seleccionada
