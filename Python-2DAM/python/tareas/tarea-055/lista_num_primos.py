usr = int(input("Introduce un entero: "))
primos = []
for i in range(usr, 1, -1):
    primo = True
    for j in range(2, ((i//2) + 1), 1):
        if i % j == 0:
            primo = False
    if primo:
        primos.append(i)
print(f"Números primos menores o igual a {usr}: {primos}")