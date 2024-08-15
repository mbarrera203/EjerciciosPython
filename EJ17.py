def empleados_con_salario_mayor(empleados, salario_minimo):
  empleados_filtrados = {}
  for id_empleado, (nombre, edad, salario) in empleados.items():
    if salario > salario_minimo:
      empleados_filtrados[id_empleado] = (nombre, edad, salario)
  return empleados_filtrados


empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

salario_minimo = 3000
empleados_alta = empleados_con_salario_mayor(empleados, salario_minimo)
print(empleados_alta)
