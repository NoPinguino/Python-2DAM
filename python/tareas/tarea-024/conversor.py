metros = int(input("Introduce una distancia en metros: "))
print(f"1. Kilómetros.")
print(f"2. Hectómetros.")
print(f"3. Decámetros.")
print(f"4. Metros (xd).")
print(f"5. Decímetros.")
print(f"6. Centímetros.")
print(f"7. Milímetros.")
unidad = int(input("¿A qué unidad quieres convertir?: "))

#Match (switch) para calcular el cambio de metros a otra unidad.
match unidad:
    case 1:
        print(f"{metros} metros son {metros * 0.001} kilómetros.")
    case 2:
        print(f"{metros} metros son {metros * 0.010} hectómetros.")
    case 3:
        print(f"{metros} metros son {metros * 0.100} decámetros.")
    case 4:
        print(f"Distancia ya dada en metros {metros}")
    case 5:
        print(f"{metros} metros son {metros * 10} decímetros.")
    case 6:
        print(f"{metros} metros son {metros * 100} centímetros.")
    case 7:
        print(f"{metros} metros son {metros * 1000} milímetros.")
    case _:
        print(f"Introduce una opción válida.")