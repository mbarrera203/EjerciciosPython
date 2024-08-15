def calcular_estadisticas_ventas(ventas_diarias):
  total_ventas = sum(ventas_diarias)
  promedio_diario = total_ventas / len(ventas_diarias)

  return total_ventas, promedio_diario

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]
total, promedio = calcular_estadisticas_ventas(ventas_diarias)

print("El total de ventas es:", total)
print("El promedio de ventas por día es:", promedio)