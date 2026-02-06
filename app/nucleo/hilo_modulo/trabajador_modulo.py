from PySide6.QtCore import QThread, Signal


class Trabajador(QThread):
    progreso = Signal(int)
    resultado = Signal(object)
    error = Signal(str)
    terminado = Signal()

    def __init__(self, funcion, *args, **kwargs):
        super().__init__()
        self.funcion = funcion
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            resultado = self.funcion(*self.args, progreso=self.progreso, **self.kwargs)
            self.resultado.emit(resultado)
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.terminado.emit()
