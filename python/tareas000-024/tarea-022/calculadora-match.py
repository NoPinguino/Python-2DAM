num1 = int(input("Introduce un número [1/2]: "))
num2 = int(input("Introduce un número [2/2]: "))
print(f"1. Suma")
print(f"2. Resta")
print(f"3. Producto")
print(f"4. División")
op = int(input(f"Introduce la operación que quieras hacer: "))
match op:
    case 1:
        print(f"El resultado es {num1 + num2}")
    case 2:
        print(f"El resultado es {num1 - num2}")
    case 3:
        print(f"El resultado es {num1 * num2}")
    case 4:
        if num2 == 0:
            print("División entre 0 no válida.")
        else:    
            print(f"El resultado es {num1 / num2}")
    case _:
        print("Valor no válido.")    