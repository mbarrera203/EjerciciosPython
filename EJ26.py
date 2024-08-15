def registro_empleado(nombre, edad, salario, **kwargs):
    empleado = {
        'Nombre': nombre,
        'Edad': edad,
        'Salario': salario
    }
    
    empleado.update(kwargs)
    
    return empleado

datos_empleado = registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789")
print(datos_empleado)
