import funciones

# Valores por defecto, se pueden cambiar antes de iniciar partida
num_impostores = 1
num_jugadores = 3
max_rondas = 3
# dificultad = "normal"


# def menu_dificultad(num_impostores, dificultad):
#     funciones.limpiar_consola()
#     print("Ajustes actuales: ")
#     print(f"- Número impostores: {num_impostores}")
#     print(f"- Número de jugadores: {num_jugadores}")
#     print(f"- Máximo de rondas: {max_rondas}")
#     print("")
#     print(
#         "¿Quieres cambiar los valores para hacerlo más difícil? (Se elegiran valores automáticamente en función de la cantidad de jugadores elegida)"
#     )
#     print("1. Elegir FÁCIL.")
#     print("2. Elegir NORMAL.")
#     print("3. Elegir DIFÍCIL.")
#     print(f"4. SALIR (dejar como {dificultad})")
#     print("")
#     opcion_dificultad = input("Elige una dificultad: ")
#     match opcion_dificultad:
#         case 1:
#             dificultad = "facil"
#             funciones.elegir_facil()
#         case 2:
#             dificultad = "normal"
#             funciones.elegir_normal()
#         case 3:
#             dificultad = "dificil"
#             funciones.elegir_dificil()
#         case 4:
#             print("Se va a volver al menu principal...")


# EL FLUJO NORMAL DEL PROGRAMA EMPIEZA AQUÍ:
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
    # print("8. Elegir dificultad.")
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
        # case "8":
        #     menu_dificultad(num_impostores, dificultad)
        #     break
        case _:
            print("ERROR: Opción inválida.")
