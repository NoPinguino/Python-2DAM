lista = [42, 17, 89, 3, 56, 78, 25, 61, 12, 34, 90, 7, 68, 22, 49, 81, 15, 97, 29, 53]
#lista = [1,2,3,4,5,6,7,8,9,10]
mediana = 0
if len(lista) % 2 == 0:
    mediana = (lista[int(len(lista) // 2)] + lista[int(len(lista) // 2 - 1)]) / 2
    print(f"La mediana es {mediana}")
else:
    mediana = lista[int(len(lista) // 2)]
    print(f"La mediana es {mediana}")