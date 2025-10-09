usr = int(input("Introduce un entero: "))
divisores = []
for i in range(usr, 1, -1):
    primo = True
    for j in range(2, ((i//2) + 1), 1):
        if i % j == 0:
            primo = False
    if primo:
        divisores.append(i)
divisores.sort()
cont_div = 0
factorizacion = []
while usr != 1:
    if usr % divisores[cont_div] == 0:
        usr = usr / divisores[cont_div] 
        factorizacion.append(divisores[cont_div])
    else:
        cont_div+=1
print(factorizacion)