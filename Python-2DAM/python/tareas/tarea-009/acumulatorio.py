num_final = int(input("Introduce el número final del sumatorio: "))
acumulatorio = 0
for i in range(num_final+1):
    acumulatorio += i
print("El acumulatorio es ",acumulatorio)