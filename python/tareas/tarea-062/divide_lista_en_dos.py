lista = [1,2,3,4,5,6,7,8,9,10]
usr = int(input("Introduce un número: "))
lista_mayor = []
lista_menor = []

for i in lista:
    if i >= usr:
        lista_mayor.append(i)
    else:
        lista_menor.append(i)

print(f"Lista mayor: {lista_mayor}.")
print(f"Lista menor: {lista_menor}.")