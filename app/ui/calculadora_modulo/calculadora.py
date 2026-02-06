class Calculadora:
    def __init__(self):
        self.reset()

    def reset(self):
        self.valor_actual = ""
        self.valor_anterior = None
        self.operacion = None
        self.resultado_mostrado = False

    def agregar_numero(self, numero):
        if self.resultado_mostrado:
            self.valor_actual = ""
            self.resultado_mostrado = False

        self.valor_actual += numero
        return self.valor_actual

    def agregar_punto(self):
        if self.resultado_mostrado:
            self.valor_actual = "0"
            self.resultado_mostrado = False

        if "." not in self.valor_actual:
            self.valor_actual = self.valor_actual or "0"
            self.valor_actual += "."
        return self.valor_actual

    def set_operacion(self, operacion):
        if self.valor_actual == "":
            self.operacion = operacion
            return str(self.valor_anterior) if self.valor_anterior is not None else "0"

        if self.valor_anterior is not None:
            self._calcular_parcial()

        self.valor_anterior = float(self.valor_actual)
        self.valor_actual = ""
        self.operacion = operacion
        return self._formatear(self.valor_anterior)

    def calcular(self):
        if self.valor_actual == "" or self.operacion is None:
            return "0"

        self._calcular_parcial()
        self.operacion = None
        self.resultado_mostrado = True
        return self._formatear(self.valor_anterior)

    def _calcular_parcial(self):
        actual = float(self.valor_actual)

        if self.operacion == "+":
            self.valor_anterior += actual
        elif self.operacion == "-":
            self.valor_anterior -= actual
        elif self.operacion == "*":
            self.valor_anterior *= actual
        elif self.operacion == "/":
            if actual == 0:
                self.reset()
                raise ZeroDivisionError

        self.valor_actual = ""

    def borrar_ultimo(self):
        if self.resultado_mostrado:
            self.reset()
            return "0"

        self.valor_actual = self.valor_actual[:-1]
        return self.valor_actual or "0"

    def _formatear(self, valor):
        if valor.is_integer():
            return str(int(valor))
        return str(valor)
