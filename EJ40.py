def simular_mercado(precios_diarios, operaciones):
    # Inicializar variables
    saldo = 0
    acciones_en_possession = 0
    precio_compra = 0
    
    # Iterar sobre las operaciones
    for operacion, dia in operaciones:
        precio = precios_diarios[dia]
        
        if operacion == "compra":
            # Si hay acciones en posesión, calcular el saldo antes de comprar
            if acciones_en_possession > 0:
                saldo -= acciones_en_possession * precio_compra
                acciones_en_possession = 0
            
            # Comprar acciones
            precio_compra = precio
            acciones_en_possession += 1
        
        elif operacion == "venta":
            # Vender las acciones compradas anteriormente
            if acciones_en_possession > 0:
                saldo += acciones_en_possession * precio - acciones_en_possession * precio_compra
                acciones_en_possession = 0
    
    # Si hay acciones sin vender, no se realiza ninguna operación para ellas
    if acciones_en_possession > 0:
        saldo -= acciones_en_possession * precio_compra
    
    return saldo

# Ejemplo de uso
precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

resultado = simular_mercado(precios_diarios, operaciones)
print(f"Beneficio o pérdida total: {resultado}")
