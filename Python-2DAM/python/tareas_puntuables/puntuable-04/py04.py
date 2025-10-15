import random

random_num = random.randint(1,10)

intentos = 1
adivinado = False
while not adivinado and intentos <= 6:
    usr = int(input("Introduce un entero: "))
    if usr == random_num:
        adivinado = True
    else:
        intentos+=1

if adivinado == True:
    print(f"Adivinaste el número en {intentos} intentos.")
else:
    print(f"No adivinaste el número en seis o menos intentos.")