def estadisticas_temperaturas(temperaturas):
  
  # Calculamos la media sumando todas las temperaturas y dividiendo por la cantidad
  media = sum(temperaturas) / len(temperaturas)

  # Encontramos la temperatura máxima y mínima usando las funciones built-in max() y min()
  maxima = max(temperaturas)
  minima = min(temperaturas)

  return media, maxima, minima

# Ejemplo de uso:
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
media, maxima, minima = estadisticas_temperaturas(temperaturas)

print("La temperatura media es:", media)
print("La temperatura máxima es:", maxima)
print("La temperatura mínima es:", minima)