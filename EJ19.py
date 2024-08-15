def calcular_goles_totales(resultados):
  goles_anotados_total = 0
  goles_recibidos_total = 0

  for resultado in resultados.values():
    goles_anotados, goles_recibidos = resultado
    goles_anotados_total += goles_anotados
    goles_recibidos_total += goles_recibidos

  return goles_anotados_total, goles_recibidos_total
resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

total_anotados, total_recibidos = calcular_goles_totales(resultados)
print("Goles anotados en total:", total_anotados)
print("Goles recibidos en total:", total_recibidos)