from collections import defaultdict

def analizar_encuestas(encuestas):
    resultados = {}
    
    for pregunta, respuestas in encuestas.items():
        
        frecuencia_respuestas = defaultdict(int)

        for respuesta in respuestas:
            frecuencia_respuestas[respuesta] += 1

        resultados[pregunta] = dict(frecuencia_respuestas)
    
    return resultados

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

resultado = analizar_encuestas(encuestas)
print(resultado)
