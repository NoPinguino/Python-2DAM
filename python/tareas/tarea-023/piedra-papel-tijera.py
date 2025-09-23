maquina = 1 #1. Piedra // 2. Papel // 3. Tijera
print(f"1 - Piedra")
print(f"2 - Papel")
print(f"3 - Tijera")
user = int(input("Introduce una opción: "))
match user:
    case 1:
        if maquina == 1:
            print(f"Empate, los dos eligieron piedra.")
        elif maquina == 2:
            print(f"Has perdido contra papel.")
        elif maquina == 3:
            print(f"Has ganado contra tijera.")
    case 2:
        if maquina == 1:
            print(f"Has ganado contra piedra.")
        elif maquina == 2:
            print(f"Empate, los dos eligieron papel.")
        elif maquina == 3:
            print(f"Has perdido contra tijera.")
    case 3:
        if maquina == 1:
            print(f"Has perdido contra piedra.")
        elif maquina == 2:
            print(f"Has ganado contra papel.")
        elif maquina == 3:
            print(f"Empate, los dos eligieron tijera.")
    case _:
        print(f"Valor inválido.")

