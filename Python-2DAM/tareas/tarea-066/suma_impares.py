lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
suma_impares = 0
for i in lista:
    if i % 2 != 0:
        suma_impares += i
print(f"La suma de los enteros de la lista: {suma_impares}")