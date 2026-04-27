from .analisis_ia_modulo import AnalisisANN
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


# installa/uninstall - > pip install scikit-learn seaborn matplotlib
def evaluar_modelo():
    # Inicializar modelo
    analizador = AnalisisANN()

    # Dataset pequeño (puedes ampliarlo si quieres)
    data = [
        ("estoy muy feliz hoy", "joy"),
        ("me siento triste", "sadness"),
        ("estoy enojado contigo", "anger"),
        ("tengo miedo de esto", "fear"),
        ("esto es increíble", "joy"),
        ("odio esto", "anger"),
        ("me siento solo", "sadness"),
        ("estoy nervioso", "fear"),
    ]

    y_true = []
    y_pred = []

    for texto, etiqueta_real in data:
        resultado = analizador.analizar_texto(texto)

        probs = resultado["probabilidades"]
        etiquetas = resultado["etiquetas"]

        pred_index = probs.argmax().item()
        pred_label = etiquetas[pred_index]

        y_true.append(etiqueta_real)
        y_pred.append(pred_label)

    # 📊 Reporte de métricas
    print("\n=== REPORTE DE CLASIFICACIÓN ===\n")
    print(classification_report(y_true, y_pred))

    # 📉 Matriz de confusión
    cm = confusion_matrix(y_true, y_pred)

    sns.heatmap(cm, annot=True, fmt="d")
    plt.title("Matriz de Confusión")
    plt.xlabel("Predicción")
    plt.ylabel("Real")
    plt.show()
