def publicar(nombre_usuario, texto_publicacion, **kwargs):
    publicacion = {
        'Nombre Usuario': nombre_usuario,
        'Texto Publicacion': texto_publicacion,
        'Etiquetas': kwargs.get('etiquetas', []),
        'Visibilidad': kwargs.get('visibilidad', 'privada'),
        'Likes': kwargs.get('likes', 0)
    }
    
    return publicacion

resultado = publicar(
    "Juan", 
    "Mi primer post!", 
    etiquetas=["#hola", "#primerPost"], 
    visibilidad="publica", 
    likes=100
)
print(resultado)
