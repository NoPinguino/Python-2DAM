numeros = [1,2,-3,3,-13,4,5,-7,6,7,8,9,-1,-5,-9,-11]
cont = 0
for i in numeros:
    if i < 0:
        cont+=1
        print(i,end=" ")
print(f"Hay {cont} números negativos")