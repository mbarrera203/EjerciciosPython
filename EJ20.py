def configurar_app(**configuraciones):

  configuraciones_defecto = {
      "modo_oscuro": False,
      "idioma": "en",
      "notificaciones": True,
  }

  # Actualizamos las configuraciones por defecto con las proporcionadas
  configuraciones_defecto.update(configuraciones)

  return configuraciones_defecto

config = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)
print(config)