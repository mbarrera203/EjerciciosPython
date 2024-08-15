def actualizar_inventario(inventario, ventas):
    # Recorremos ambos arrays simultáneamente
    for i in range(len(inventario)):
        inventario[i] -= ventas[i]  # Restamos las ventas al inventario
    
    return inventario

# Array de inventario inicial
inventario = [50, 30, 20, 10]

# Array de ventas realizadas
ventas = [5, 10, 5, 2]

inventario_actualizado = actualizar_inventario(inventario, ventas)

print(inventario_actualizado)
