producto = ""
productos = {}
while producto != "fin":
    producto = input("Introduce un nombre: ")
    cantidad = int(input("Introduce un cantidad: "))
    if producto != "fin":
        productos[producto] = cantidad
print(productos)