def calcular_precios_totales(paquetes):
    precios_totales = {}  

    for destino, precio, duracion in paquetes:
        precio_total = precio * duracion  # Calcula el precio total para el destino
        precios_totales[destino] = precio_total  # Asigna el precio total al destino en el diccionario

    return precios_totales

# Lista de paquetes turísticos
paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

# Llamada a la función y almacenamiento del resultado
resultados = calcular_precios_totales(paquetes)

# Imprime el diccionario resultante
print(resultados)
