#Importo el paquete funciones
import funciones
#Variable de control, mientras sea False no se inicia la partida porque el jugador aún no ha introducido un modo de juego válido
modo_valido = False
while not modo_valido:
    #Imprimo los modos de juego para que el jugador pueda seleccionar
    print("1. Jugador contra Jugador")
    print("2. Jugador contra Máquina")
    print("3. Máquina contra Máquina")
    #Pido al usuario que introduzca el modo de juego.
    modo_de_juego = int(input("Selecciona el modo de juego: "))
    #En un match llamo a las funciones de cada modo de juego, en caso de que no sea un modo válido, vuelve a pedir al usuario que ponga un modo válido
    match(modo_de_juego):
        case 1:
            #Rompo el bucle cambiando el valor de la variable de control e inicio partida llamando a la función correspondiente
            modo_valido = True
            funciones.JugadorContraJugador()
        case 2:
            #Rompo el bucle cambiando el valor de la variable de control e inicio partida llamando a la función correspondiente
            modo_valido = True
            funciones.JugadorContraMaquina()
        case 3:
            #Rompo el bucle cambiando el valor de la variable de control e inicio partida llamando a la función correspondiente
            modo_valido = True
            funciones.MaquinaContraMaquina()
        case _:
            #Caso default en la situacion de que el modo_de_juego no sea válido, se imprime un mensaje y pide que introduzca un número válido
            print("⚠️ - Modo de juego no válido. Introdcelo de nuevo.")