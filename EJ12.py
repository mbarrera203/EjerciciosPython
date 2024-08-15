def producto_mas_caro(lista_productos):
  producto_mas_caro = max(lista_productos, key=lambda x: x[1])
  return producto_mas_caro

productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]
resultado = producto_mas_caro(productos)
print("El producto más caro es:", resultado)
