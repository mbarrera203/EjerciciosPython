def actualizar_suscripcion(suscripciones, usuario, suscripcion, **kwargs):

    if usuario not in suscripciones:
        suscripciones[usuario] = []
       
    suscripciones[usuario].append(suscripcion) 
   
    opciones_adicionales = {}
    for clave, valor in kwargs.items():
        opciones_adicionales[clave] = valor
    
    
    return {
        'suscripciones': suscripciones,
        'opciones_adicionales': opciones_adicionales
    }
suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}
resultado = actualizar_suscripcion(suscripciones, usuario="Luis", suscripcion="mensual", auto_renovacion=True)
print(resultado)
