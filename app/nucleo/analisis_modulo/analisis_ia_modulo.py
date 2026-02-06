import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class AnalisisANN:
    def __init__(self):
        self._NOMBRE_MODELO = "finiteautomata/beto-emotion-analysis"
        self._tokenizador = AutoTokenizer.from_pretrained(self._NOMBRE_MODELO)
        self._modelo = AutoModelForSequenceClassification.from_pretrained(
            self._NOMBRE_MODELO
        )

    def analizar_texto(self, texto):
        entradas = self._tokenizador(
            texto, return_tensors="pt", truncation=True, padding=True, max_length=128
        )

        with torch.no_grad():
            salidas = self._modelo(**entradas)

        probabilidades = torch.softmax(salidas.logits, dim=1)
        etiquetas = self._modelo.config.id2label

        resultado = {"probabilidades": probabilidades[0], "etiquetas": etiquetas}

        return resultado
