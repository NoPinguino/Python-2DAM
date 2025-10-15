num = int(input("Introduce un entero: "))
primo = True
for i in range(2, ((num//2) + 1)):
    if num % i == 0:
        primo = False
if primo == True:
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")