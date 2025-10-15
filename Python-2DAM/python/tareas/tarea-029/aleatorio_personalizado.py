import random
limitInf = int(input("Introduce el límite inferior: "))
limitSup = int(input("Introduce el límite superior: "))
cantidad = int(input("Cantidad de números aleatorios: "))
if limitInf <= limitSup:
    for i in range(cantidad):
        aleatorio = random.randint(limitInf, limitSup)
        print(aleatorio)
else:
    print("El número inferior debe ser inferior al superior.")