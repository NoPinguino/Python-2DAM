lista = [5, 12, 37, 48, 3, 89, 24, 76, 55, 61, 9, 30, 42, 18, 97, 70, 66, 81, 25, 33]
lista_invertida = []
contador = len(lista) - 1
while len(lista) > len(lista_invertida):
    lista_invertida.append(lista[contador])
    contador-=1
print(lista_invertida)