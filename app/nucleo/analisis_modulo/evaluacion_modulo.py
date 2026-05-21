from .analisis_ia_modulo import AnalisisANN
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


def evaluar_modelo():
    # Inicializar modelo
    analizador = AnalisisANN()

    # Dataset de pruebas
    data = [
        # JOY
        ("estoy muy feliz hoy", "joy"),
        ("esto es increíble", "joy"),
        ("me siento contento con mi vida", "joy"),
        ("todo salió perfecto y estoy encantado", "joy"),
        ("qué día tan maravilloso", "joy"),
        ("no puedo dejar de sonreír", "joy"),
        # SADNESS
        ("me siento triste", "sadness"),
        ("me siento solo", "sadness"),
        ("hoy ha sido un día muy duro", "sadness"),
        ("extraño mucho esos momentos", "sadness"),
        ("me siento vacío por dentro", "sadness"),
        ("nada me motiva últimamente", "sadness"),
        # ANGER
        ("estoy enojado contigo", "anger"),
        ("odio esto", "anger"),
        ("esto me saca de quicio", "anger"),
        ("no soporto esta situación", "anger"),
        ("me irrita que pase esto", "anger"),
        ("estoy furioso por lo ocurrido", "anger"),
        # FEAR
        ("tengo miedo de esto", "fear"),
        ("estoy nervioso", "fear"),
        ("siento que algo malo va a pasar", "fear"),
        ("me da pánico intentarlo", "fear"),
        ("no me siento seguro aquí", "fear"),
        ("estoy preocupado por el futuro", "fear"),
        # SURPRISE
        ("no me esperaba esto para nada", "surprise"),
        ("qué sorpresa tan grande", "surprise"),
        ("esto me dejó sin palabras", "surprise"),
        ("no puedo creer lo que pasó", "surprise"),
        ("esto fue totalmente inesperado", "surprise"),
        ("es algo que no me imaginaba", "surprise"),
    ]

    y_true = []
    y_pred = []

    resultado = None

    for texto, etiqueta_real in data:
        resultado = analizador.analizar_texto(texto)

        probs = resultado["probabilidades"]
        etiquetas = resultado["etiquetas"]

        pred_index = probs.argmax().item()
        pred_label = etiquetas[pred_index]

        y_true.append(etiqueta_real)
        y_pred.append(pred_label)

    print("\n--> REPORTE DE CLASIFICACIÓN <--\n")
    print(classification_report(y_true, y_pred, labels=resultado["etiquetas"]))

    # Matriz de confusion
    cm = confusion_matrix(y_true, y_pred)

    sns.heatmap(cm, annot=True, fmt="d")
    plt.title("Matriz de Confusión")
    plt.xlabel("Predicción")
    plt.ylabel("Real")
    plt.show()


# installa/uninstall - > pip install scikit-learn seaborn matplotlib
