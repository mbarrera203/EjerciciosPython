def libros_post_2000(biblioteca):
    libros_recientes = []
    
    for titulo, info in biblioteca.items():
        #
        if info['año'] > 2000:
            libros_recientes.append(titulo)
    
    return libros_recientes

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

resultados = libros_post_2000(biblioteca)
print(resultados)
