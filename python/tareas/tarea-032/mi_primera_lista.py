lista = []
seguir = True
while True:
    user = int(input("Introduce un entero, 0 para salir: "))
    if user == 0:
        break
    else:
        lista.append(user)
print(f"Lista: {lista}")
print(f"Primer elemento: {lista[0]}")
print(f"Último elemento: {lista[-1]}")