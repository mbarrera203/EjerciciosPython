from collections import Counter

def analizar_tendencias(hashtags, tendencias):
    # Contar la frecuencia de cada hashtag en el array de hashtags
    conteo_hashtags = Counter(hashtags)
    
    # Crear un diccionario de frecuencias para facilitar la búsqueda
    frecuencias = dict(tendencias)
    
    # Filtrar hashtags que tienen una frecuencia mayor que el umbral especificado
    hashtags_filtrados = {
        hashtag: conteo
        for hashtag, conteo in conteo_hashtags.items()
        if hashtag in frecuencias and conteo > frecuencias[hashtag]
    }
    
    return hashtags_filtrados

# Ejemplo de uso
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

resultado = analizar_tendencias(hashtags, tendencias)
print(resultado)
