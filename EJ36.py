def filtrar_rutas(rutas, distancias_max):
    rutas_filtradas = []
    
    
    if len(rutas) != len(distancias_max):
        raise ValueError("El número de distancias máximas debe coincidir con el número de rutas")
    
   
    for ruta, distancia_max in zip(rutas, distancias_max):
        origen, destino, distancia = ruta
        
        # Verificar si la distancia cumple con la distancia máxima permitida
        if distancia <= distancia_max:
            rutas_filtradas.append(ruta)
    
    return rutas_filtradas


rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

resultado = filtrar_rutas(rutas, distancias_max)
print(resultado)
