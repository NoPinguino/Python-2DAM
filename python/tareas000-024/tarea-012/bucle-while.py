num = int(input("Introduce un entero (0 para cerrar): "))
sumatorio = 0
while num != 0:
    sumatorio += num
    num = int(input("Introduce un entero (0 para cerrar): "))
print(f"El sumatorio es {sumatorio}")    