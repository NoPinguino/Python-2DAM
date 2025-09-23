import random
#Bogo sort
lista = [5, 2, 9, 1, 5, 6]
intentos = 0
ordenado = False
seleccion = input("ascendente o descendente: ").lower()
if seleccion == "ascendente":
    while not ordenado:
        intentos+=1
        ordenado = True
        for i in range(1,len(lista)):
            if lista[i] < lista[i - 1]:
                ordenado = False
                break
        if not ordenado:
            random.shuffle(lista)
    print(f"Lista: {lista}")
    print(f"Se ha ordenado en {intentos} intentos.")
elif seleccion == "descendente":
    while not ordenado:
        intentos+=1
        ordenado = True
        for i in range(1,len(lista)):
            if lista[i] > lista[i - 1]:
                ordenado = False
                break
        if not ordenado:
            random.shuffle(lista)
    print(f"Lista: {lista}")
    print(f"Se ha ordenado en {intentos} intentos.")
else:
    print("Opción inválida")