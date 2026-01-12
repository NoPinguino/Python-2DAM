producto = {
    "Nombre": "Calcetines",
    "Precio": 12.50,
    "Stock": 10
}

nuevo_precio = int(input("Introduce un nuevo precio: "))
producto.update({
    "Precio": nuevo_precio,
})

print(producto)