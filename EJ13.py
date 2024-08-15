def promedio_calificaciones(estudiantes, matricula):

  if matricula in estudiantes:
    calificaciones = estudiantes[matricula]["calificaciones"]
    promedio = sum(calificaciones.values()) / len(calificaciones)
    return promedio
  else:
    return None

# Ejemplo de uso:
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

matricula_buscada = 101
promedio = promedio_calificaciones(estudiantes, matricula_buscada)

if promedio:
  print(f"El promedio de calificaciones de {estudiantes[matricula_buscada]['nombre']} es {promedio:.2f}")
else:
  print("No se encontró al estudiante.")
