import random
import funciones

#Creo el tablero como una lista global para acceder desde todas las funciones

#Selección de modo de juego:
modo_valido = False

#funciones.SeleccionarIconos()

while not modo_valido:
    print("1. Jugador contra Jugador")
    print("2. Jugador contra Máquina")
    print("3. Máquina contra Máquina")
    #Pido al usuario que introduzca el modo de juego.
    modo_de_juego = int(input("Selecciona el modo de juego: "))

    #En un match llamo a las funciones de cada modo de juego, en caso de que no sea un modo válido, vuelve a pedir al usuario que ponga un modo válido
    match(modo_de_juego):
        case 1:
            modo_valido = True
            funciones.SeleccionarIconos()
            funciones.JugadorContraJugador()
        case 2:
            modo_valido = True
            JugadorContraMaquina()
        case 3:
            modo_valido = True
            MaquinaContraMaquina()
        case _:
            print("⚠️ - Modo de juego no válido. Introdcelo de nuevo.")