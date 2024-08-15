def estadisticas_ventas(ventas_mensuales):

    total_ventas = sum(ventas_mensuales)
    promedio_mensual = total_ventas / len(ventas_mensuales) 
    mes_max_ventas = ventas_mensuales.index(max(ventas_mensuales)) + 1  

    return {
        'Total Ventas': total_ventas,
        'Promedio Mensual': promedio_mensual,
        'Mes con Mayores Ventas': mes_max_ventas
    }


ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
resultados = estadisticas_ventas(ventas_mensuales)
print(resultados)
