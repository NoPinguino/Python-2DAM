secreto = 67
intentos = 0
num = 0
while num != secreto and intentos < 6:
    num = int(input("Adivina el número secreto: "))
    if num == secreto:
        print(f"Número secreto adivinado ({secreto} en {intentos} intentos.)")
    else:
        intentos+=1  
if intentos >= 6:
    print("Intentos máximos excedidos.")