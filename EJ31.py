def calcular_promedio_general(estudiantes):
    promedios = {}
    
    for id_estudiante, materias in estudiantes.items():
        total_calificaciones = 0
        num_calificaciones = 0
        
       
        for calificaciones in materias.values():
            total_calificaciones += sum(calificaciones)
            num_calificaciones += len(calificaciones)
        
       
        promedio_general = total_calificaciones / num_calificaciones
        promedios[id_estudiante] = promedio_general
    
    
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    
    return ranking

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

resultado = calcular_promedio_general(estudiantes)
print(resultado)
