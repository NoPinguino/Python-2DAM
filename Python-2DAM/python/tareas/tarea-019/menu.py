opcion_elegida = int(input("Elige opción: 1=Saludar, 2=Despedirse, 3=Salir: "))
match opcion_elegida:
    case 1:
        print("¡Hola!")
    case 2:
        print("¡Adiós!")
    case 3:
        print("Me piro...")
    case _:
        print("Elige una buena, por favor")