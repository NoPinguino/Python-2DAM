import random
secreto = random.randint(1,10)
intento = 0
adivinado = False
while (intento < 6 and adivinado == False):
    user = int(input("Adivina el número secreto: "))
    if (user == secreto):
        adivinado = True
    intento+=1
if adivinado and intento < 6:
    print(f"Has adivinado el número en {intento}")
else:
    print(f"No adivinaste el número, era {secreto}")