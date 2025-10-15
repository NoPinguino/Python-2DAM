lista = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
find_num = int(input("Número a buscar: "))
new_num = int(input("Número por el que será reemplazado: "))
for i in range(len(lista)):
    if lista[i] == find_num:
        lista[i] = new_num
print(lista)