def configurar_perfiles(usuarios, **kwargs):
    
    perfiles = {}
    configuraciones = list(kwargs.values())
    for usuario in usuarios:
        perfiles[usuario] = configuraciones
    return perfiles


usuarios = ["Ana", "Luis", "María"]
resultados = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
print(resultados)
