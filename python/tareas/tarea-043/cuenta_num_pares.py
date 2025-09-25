lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
pares = 0
impares = 0
for i in lista:
    if i % 2 == 0:
        pares+=1
    else:
        impares+=1
print(f"Se han encontrado {pares} números pares.")
print(f"Se han encontrado {impares} números impares.")