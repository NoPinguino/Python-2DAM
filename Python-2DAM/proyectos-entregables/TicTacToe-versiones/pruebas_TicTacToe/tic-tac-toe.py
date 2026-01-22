import random

#Creo la lista anidada en la que se actualizará cada ve que se haga un movimiento.
tablero = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
#Función que imprime el estado actual de el tablero
def imprimirTablero():
    print("  | 1 | 2 | 3 |")
    for i in range(len(tablero)):
        print("---------------")
        print(i+1,end=" | ")
        for j in tablero[i]:
            print(j,end=" | ")
        print(" ")
#Función para validar si la posición está disponible o no
def validarPos(fila,col):
    if (fila >= 0 and fila < len(tablero[0])) and (col >= 0 and col < len(tablero)):
        if tablero[fila][col] == " ":
            return True
        else:
            return False
    else:
        return False
#Función para despejar la consola
def limpiarConsola():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
#Función que comprueba si algún jugador ha ganado
def comprobarGanado():
    ganado = " "
    for i in range(3):
        #Caso 1: victoria horizontal
        if ((tablero[i][0] == tablero[i][1]) and (tablero[i][0] == tablero[i][2])) and tablero[i][0] != " ":
            ganado = tablero[i][0]
        #Caso 2: Victoria vertical
        if ((tablero[0][i] == tablero[1][i]) and  (tablero [0][i] == tablero[2][i])) and tablero[0][i] != " ":
            ganado = tablero[0][i]
    #Caso 3: victoria diagonal
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[1][1] != " ":
        ganado = tablero[1][1]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[1][1] != " ":
        ganado = tablero[1][1]
    return ganado
#Función que controla todo lo que tiene que ver con el modo de juego Jugador contra Jugador
def JugContraJug():
    #Variables esenciales para el juego
    turno = 0
    acabar = False
    #Bucle de juego
    while acabar == False:
        #Cumpruebo que haya espacios libros
        if (" " not in tablero[0]) and (" " not in tablero[1]) and (" " not in tablero[2]):
            print("El tablero ya está lleno.")
            acabar = True
            #La forma que tengo de diferenciar si se ha ganado por victoria real o por falta de movimientos es estableciendo los turnos en negativos en caso de que sea por falta de movimientos
            turno = -1
        #Inicio la iteración de juego en caso de que aún haya espacios libres para jugar
        else:
            if turno % 2 == 0:
                #Jugador X:
                imprimirTablero()
                valido = False
                while not valido: 
                    #Pido posición al usuario y la valido:
                    print("Turno de Jugador[X]")
                    fila = (int(input("Introduce la fila: ")) - 1)
                    col = (int(input("Introduce la columna: ")) - 1)
                    valido = validarPos(fila,col)
                    if valido == False:
                        print("⚠️ - Posición ya ocupada o no válida.")
                    else:
                        #En caso de que la posición sea válida, se guarda el movimiento:
                        tablero[fila][col] = "x"
            else:
                #Jugador O
                imprimirTablero()
                valido = False
                while not valido:
                    #Pido posición al usuario y la valido:
                    print("Turno de jugador[O]")
                    fila = (int(input("Introduce la fila: ")) - 1)
                    col = (int(input("Introduce la columna: ")) - 1)
                    valido = validarPos(fila,col)
                    if valido == False:
                        print("⚠️ - Posición ya ocupada o no válida.")
                    else:
                        #En caso de que la posición sea válida, se guarda el movimiento:
                        tablero[fila][col] = "o"
        #Cumpruebo si la partida debería de terminar por victoria
        ganado = comprobarGanado()
        if ganado != " " and acabar == False:
            acabar = True
        #Sumo turno y limpio consola para legibilidad en la próxima iteración
        turno+=1
        limpiarConsola()
    #Imprimo el estado final del tablero y quién ha ganado en caso de que haya ganador
    imprimirTablero()
    if turno % 2 == 1 and turno > 0:
        print("Ganó el Jugador X")
    elif turno % 2 == 0 and turno > 0:
        print("Ganó el jugador O")
    else:
        print("⚠️ ¡EMPATE! ⚠️")
#Función que controla todo lo que tiene que ver con el modo de juego Jugador contra Máquina
def JugContraMaq():
    turno = 0
    acabar = False
    while acabar == False:
        if turno % 2 == 0:
            #Jugador X:
            imprimirTablero()
            valido = False
            while not valido: 
                #Pido posición al usuario y la valido:
                print("Turno de Jugador[X]")
                fila = (int(input("Introduce la fila: ")) - 1)
                col = (int(input("Introduce la columna: ")) - 1)
                valido = validarPos(fila,col)
                if valido == False:
                    print("⚠️ - Posición ya ocupada o no válida.")
                else:
                    #En caso de que la posición sea válida, se guarda el movimiento:
                    tablero[fila][col] = "x"
        else:
            #Jugador O (máquina):
            imprimirTablero()
            valido = False
            while not valido:
                #Genero posición aleatoria:
                fila = random.randint(0,len(tablero))
                col = random.randint(0,len(tablero[0]))
                valido = validarPos(fila,col)
                #En caso de que las posiciones generadas aleatoriamente sean válidas, se dibuja en el tablero
                if valido:
                    tablero[fila][col] = "o"
        ganado = comprobarGanado()
        if ganado != " " and acabar == False:
            acabar = True
        #Sumo turno y limpio consola para legibilidad en la próxima iteración
        turno+=1
        limpiarConsola()  
    #Imprimo el estado final del tablero y quién ha ganado en caso de que haya ganador
    imprimirTablero()
    if turno % 2 == 1 and turno > 0:
        print("Ganó el Jugador X")
    elif turno % 2 == 0 and turno > 0:
        print("Ganó el jugador O")
    else:
        print("⚠️ ¡EMPATE! ⚠️")

#Función que controla todo lo que tiene que ver con el modo de juego Máquina contra Máquina
def MaqContraMaq():
    turno = 0
    acabar = False
    while not acabar:
        if turno % 2 == 0:
            #Jugador X (máquina):
            imprimirTablero()
            valido = False
            while not valido:
                #Genero posición aleatoria:
                fila = random.randint(0,len(tablero))
                col = random.randint(0,len(tablero[0]))
                valido = validarPos(fila,col)
                #En caso de que las posiciones generadas aleatoriamente sean válidas, se dibuja en el tablero
                if valido:
                    tablero[fila][col] = "x"
        else:
            #Jugador O (máquina):
            imprimirTablero()
            valido = False
            while not valido:
                #Genero posición aleatoria:
                fila = random.randint(0,len(tablero))
                col = random.randint(0,len(tablero[0]))
                valido = validarPos(fila,col)
                #En caso de que las posiciones generadas aleatoriamente sean válidas, se dibuja en el tablero
                if valido:
                    tablero[fila][col] = "o"
        ganado = comprobarGanado()
        if ganado != " " and acabar == False:
            acabar = True
        #Sumo turno y limpio consola para legibilidad en la próxima iteración
        turno+=1
        limpiarConsola()  
    #Imprimo el estado final del tablero y quién ha ganado en caso de que haya ganador
    imprimirTablero()
    if turno % 2 == 1 and turno > 0:
        print("Ganó el Jugador X")
    elif turno % 2 == 0 and turno > 0:
        print("Ganó el jugador O")
    else:
        print("⚠️ ¡EMPATE! ⚠️")

#Menú de selección de modo de juego.
print("1 - Jugador contra Jugador")
print("2 - Jugador contra Máquina")
print("3 - Máquina contra Máquina")
modo = int(input("Selecciona el modo de juego: "))
match(modo): 
    case 1:
        JugContraJug()
    case 2:
        JugContraMaq()
    case 3:
        MaqContraMaq()
    case _:
        print("Modo no válido.")