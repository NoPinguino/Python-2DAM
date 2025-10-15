num = int(input("Introduce un entero (a ser posible pequeño): "))
factorial = 1
for num in range(num, 1, -1):
    print(f"{factorial}")
    factorial = factorial * num
print(f"El factorial es {factorial}.")