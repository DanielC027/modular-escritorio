from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot, Signal
from .calculadora_mainwindow_ui import Ui_MainWindow
from .calculadora import Calculadora


class UiInterfazCalculadora(QMainWindow):
    iniciar_sistema = Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.calc = Calculadora(self.iniciar_sistema)

        # ===== Numeros =====
        self.ui.pushButton_cero.clicked.connect(lambda: self.numero("0"))
        self.ui.pushButton_uno.clicked.connect(lambda: self.numero("1"))
        self.ui.pushButton_dos.clicked.connect(lambda: self.numero("2"))
        self.ui.pushButton_tres.clicked.connect(lambda: self.numero("3"))
        self.ui.pushButton_cuatro.clicked.connect(lambda: self.numero("4"))
        self.ui.pushButton_cinco.clicked.connect(lambda: self.numero("5"))
        self.ui.pushButton_seis.clicked.connect(lambda: self.numero("6"))
        self.ui.pushButton_siete.clicked.connect(lambda: self.numero("7"))
        self.ui.pushButton_ocho.clicked.connect(lambda: self.numero("8"))
        self.ui.pushButton_nueve.clicked.connect(lambda: self.numero("9"))

        # ===== Punto =====
        self.ui.pushButton_punto.clicked.connect(self.PuntoClick)

        # ===== Operaciones =====
        self.ui.pushButton_mas.clicked.connect(lambda: self.operacion("+"))
        self.ui.pushButton_menos.clicked.connect(lambda: self.operacion("-"))
        self.ui.pushButton_multiplicacion.clicked.connect(lambda: self.operacion("*"))
        self.ui.pushButton_division.clicked.connect(lambda: self.operacion("/"))

        # ===== Acciones =====
        self.ui.pushButton_igual.clicked.connect(self.IgualClick)
        self.ui.pushButton_eliminar_de_operacion.clicked.connect(self.BorrarTodo)
        self.ui.pushButton_eliminar_caracter.clicked.connect(self.BorrarCaracter)

    # ===== Util =====
    def mostrar(self, texto):
        self.ui.lineEdit_contenido.setText(texto)

    # ===== Slots =====
    @Slot()
    def numero(self, n):
        self.mostrar(self.calc.agregar_numero(n))

    @Slot()
    def PuntoClick(self):
        self.mostrar(self.calc.agregar_punto())

    @Slot()
    def operacion(self, op):
        self.mostrar(self.calc.set_operacion(op))

    @Slot()
    def IgualClick(self):
        self.mostrar(self.calc.calcular())

    @Slot()
    def BorrarTodo(self):
        self.calc.reset()
        self.mostrar("0")

    @Slot()
    def BorrarCaracter(self):
        self.mostrar(self.calc.borrar_ultimo())
