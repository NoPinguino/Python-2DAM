nota = int(input("Introduce la nota del exámen: "))
match nota:
    case 0 | 1 | 2:
        print("Muy deficiente.")
    case 3 | 4:
        print("Suspenso.")
    case 5:
        print("Aprobado.")
    case 6:
        print("Bien.")
    case 7 | 8:
        print("Notable.")
    case 9:
        print("Sobresaliente.")
    case 10:
        print("Matrícula de Honor.")
    case _:
        print("Introduce una nota válida.")