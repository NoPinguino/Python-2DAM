import funciones

# Valores por defecto, se pueden cambiar antes de iniciar partida
num_impostores = 1
num_jugadores = 3
max_rondas = 3

while True:
    print("")
    print("=== MENÚ PRINCIPAL ===")
    print("1. Seleccionar número de jugadores.")
    print("2. Seleccionar número de impostores.")
    print("3. Seleccionar número de rondas máximo.")
    print("4. Seleccionar nombre de jugadores.")
    print("5. Iniciar partida.")
    print("6. Imprimir marcador de puntuaciones.")
    print("7. SALIR")
    print("======================")
    print("")
    match_option = input("¿Qué desea hacer?: ")

    match match_option:
        case "1":
            num_jugadores = funciones.selec_num_jugadores()
        case "2":
            num_impostores = funciones.selec_num_impostores(num_jugadores)
        case "3":
            max_rondas = funciones.selec_max_rondas(num_impostores)
        case "4":
            funciones.selec_nombre_jugadores(num_jugadores)
        case "5":
            funciones.partida(num_impostores, max_rondas)
        case "6":
            funciones.imprimir_marcador()
        case "7":
            input("👋 - Cerrando el juego...")
            break
        case _:
            print("ERROR: Opción inválida.")
