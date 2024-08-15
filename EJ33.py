def simular_ventas(*args):
    total_ingresos = 0.0
    
    
    for venta in args:
        producto, cantidad_vendida, precio_por_unidad = venta
        total_ingresos += cantidad_vendida * precio_por_unidad
    
    return total_ingresos

resultado = simular_ventas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
)
print(f"Total de ingresos generados: ${resultado:.2f}")
