lista = [1,1,2,3,3,3,4,4,5,6,7,7,7,7,8,9]
lista_contada = []
nums = []
lista.sort()
print(lista)
for i in lista:
    contador = 0
    if i not in nums:
        for j in lista:
            if i == j:
                contador+=1
        lista_contada.append((i,contador))
        nums.append(i)
print(lista_contada)