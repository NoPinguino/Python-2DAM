print(f"L - Lunes")
print(f"M - Martes")
print(f"X - Miércoles")
print(f"J - Jueves")
print(f"V - Viernes")
print(f"S - Sábado")
print(f"D - Domingo")
dia = input(f"Introduce el día de la semana: ").upper()
match dia:
    case "L":
        print("Es laborable.")
    case "M":
        print("Es laborable.")
    case "X":
        print("Es laborable.")
    case "J":
        print("Es laborable.")
    case "V":
        print("Es laborable.")
    case "S":
        print("Es fin de semana.")
    case "D":
        print("Es fin de semana.")
    case _:
        print("Introduce un día válido.")