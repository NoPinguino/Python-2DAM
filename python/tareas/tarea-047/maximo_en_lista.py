lista = [1,3,2,6,4,5,8,9,10,12,3,7,8]
maximo = lista[0]
for i in lista:
    if i > maximo:
        maximo = i
print(f"Máximo: {maximo}")