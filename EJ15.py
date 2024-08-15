def calcular_promedio(*notas):

  if notas:  
    return sum(notas) / len(notas)
  else:
    return None  

promedio = calcular_promedio(85, 90, 78, 92)
print("El promedio es:", promedio)