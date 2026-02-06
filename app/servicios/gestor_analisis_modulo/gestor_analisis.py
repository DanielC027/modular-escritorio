# from ...nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN

from nucleo.analisis_modulo.analisis_ia_modulo import AnalisisANN


class GestorAnalisis:
    def analizar_texto(self, texto, progreso=None):
        analisis = AnalisisANN()
        resultado = analisis.analizar_texto(texto)
        return resultado
