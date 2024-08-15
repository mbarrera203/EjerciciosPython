def hacer_reserva(reservas, fecha, nombre_huesped, habitacion, precio):
    
    if fecha not in reservas:
        reservas[fecha] = []
    
    
    for reserva in reservas[fecha]:
        if reserva[1] == habitacion:
            return f"La habitación {habitacion} ya está ocupada en la fecha {fecha}."
    
   
    reservas[fecha].append((nombre_huesped, habitacion, precio))
    return f"Reserva realizada con éxito para {nombre_huesped} en la habitación {habitacion} en la fecha {fecha}."

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}


resultado = hacer_reserva(reservas, "2024-08-15", "Marta", 103, 200)
print(resultado)


resultado = hacer_reserva(reservas, "2024-08-15", "Carlos", 101, 160)
print(resultado)


resultado = hacer_reserva(reservas, "2024-08-17", "Sofia", 104, 170)
print(resultado)

print(reservas)