def crear_perfil(nombre, edad, email, **datos_adicionales):

  perfil = {
      "nombre": nombre,
      "edad": edad,
      "email": email,
  }

  perfil.update(datos_adicionales)  

  return perfil

perfil_usuario = crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza", telefono="12345678")

print("Perfil de usuario:", perfil_usuario)
