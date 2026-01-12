#Paquete random, necesario para la función GenerarPosicionesRandom() que utiliza la máquina al jugar
import random
#Funciones que usa el juego
tablero = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
iconPlayer1 = "x"
iconPlayer2 = "o"



#Función simple que imprime cinco líneas en blanco, usada para ver la terminal con mayor claridad
def LimpiarTerminal():
    for i in range(5):
        print()



#Función ImprimirTablero(), es de las más importantes y que más veces se usan, imprime el estado actual del tablero
def ImprimirTablero():
    #Imprime la cabecera del tablero:
    for i in range(len(tablero[0]) + 1):
        if i == 0:
            #Deja la primera posición de la cabecera en blanco porque debajo van los indicadores de las filas
            print(f"   | ",end="")
        else:
            #Imprime los indicadores de las columnas, siendo <i> el número de la columna
            print(f"{i} | ",end="")

    #Imprime el contenido del tablero:
    #La variable contador_filas nos permite imprimir al inicio de la fila el indicador de en qué fila estamos
    contador_filas = 1
    for fila in tablero:
        #Imprimo una fila de guiones para separar las filas del tablero
        print(f"\n{'-' * ((len(tablero[0]) + 1) * 4)}")
        #Imprimo el indicador de la fila
        print(f" {contador_filas} | ",end="")
            #Aumento contador filas porque ya se ha impreso el indicador
        contador_filas+=1
        #Imprimo la fila:
        for elemento in fila:
            print(f"{elemento} | ",end="")
    print()



#Función a la que llamo tras cada movimiento realizado ya sea por el jugador o por la máquina, comprueba si alguien ya ha ganado y, por lo tanto, la partida debería terminar
def ComprobarVictoria():
    #Como es el tres en raya, buscamos que tres fichas seguidas sean iguales (x/o)
    fichas_para_ganar = 3
    #Nos guardamos la cantidad de columnas y filas que tiene nuestro tablero
    columnas = len(tablero[0])
    filas = len(tablero)

    #=======================================
    #CASO DE VICTORIA POR FILA (HORIZONTAL):
    #=======================================
    for fila in range(filas):
        #Simbolo guarda el simbolo encontrado al recorrer el tablero, normalmente, el de la posición (i - 1) para poder compararlo con la posición actual y ver si hay racha o no
        simbolo = None
        #Fichas_en_raya guarda la racha de símbolos iguales seguidos
        fichas_en_raya = 0
        #Recorre las posiciones de la fila en la que nos encontramos
        for col in range(columnas):
            #Guardamos el elemento de la posición actual
            elemento = tablero[fila][col]
            #Si en la posición no hay un espacio, miramos que elemento es, si hay un espacio, nos da igual y saltamos a la próxima posición de la fila
            if elemento != " ":
                if elemento == simbolo:
                    #Si el elemento es el mismo que había en la posición anterior, sumamos a la racha
                    fichas_en_raya += 1
                else:
                    #Si el elemento es distinto al de la posición anterior, establecemos racha en 1 y nos guardamos el valor como <símbolo>
                    simbolo = elemento
                    fichas_en_raya = 1
                # En caso de que la racha sea igual a fichas_para_ganar, devuelve True (indica que la partida debe acabar) y el símbolo del ganador, para imprimirlo en consola
                if fichas_en_raya == fichas_para_ganar:
                    return True, simbolo
            else:
                simbolo = None
                fichas_en_raya = 0

    #========================================
    #CASO DE VICTORIA POR COLUMNA (VERTICAL):
    #========================================
    for col in range(columnas):
        #Simbolo guarda el simbolo encontrado al recorrer el tablero, normalmente, el de la posición (i - 1) para poder compararlo con la posición actual y ver si hay racha o no
        simbolo = None
        #Fichas_en_raya guarda la racha de símbolos iguales seguidos
        fichas_en_raya = 0
        #Recorre las posiciones de la columna en la que nos encontramos
        for fila in range(filas):
            #Guardamos el elemento de la posición actual
            elemento = tablero[fila][col]
            #Si en la posición no hay un espacio, miramos que elemento es, si hay un espacio, nos da igual y saltamos a la próxima posición de la columna
            if elemento != " ":
                if elemento == simbolo:
                    #Si el elemento es el mismo que había en la posición anterior, sumamos a la racha
                    fichas_en_raya += 1
                else:
                    #Si el elemento es distinto al de la posición anterior, establecemos racha en 1 y nos guardamos el valor como <símbolo>
                    simbolo = elemento
                    fichas_en_raya = 1
                # En caso de que la racha sea igual a fichas_para_ganar, devuelve True (indica que la partida debe acabar) y el símbolo del ganador, para imprimirlo en consola
                if fichas_en_raya == fichas_para_ganar:
                    return True, simbolo
            else:
                simbolo = None
                fichas_en_raya = 0

    # ========================================
    # CASO DE VICTORIA POR DIAGONAL PRINCIPAL:
    # ========================================
    #Iniciamos en una fila, y dentro de esa fila vamos creando diagonales del tamaño fichas_para_ganar por cada columna
    for fila_inicio in range(filas - fichas_para_ganar + 1):
        for col_inicio in range(columnas - fichas_para_ganar + 1):
            #Simbolo guarda el símbolo encontrado al recorrer el tablero, normalmente el de la posición (i - 1) para poder compararlo con la posición actual y ver si hay racha o no
            simbolo = None
            #Fichas_en_raya guarda la racha de símbolos iguales seguidos
            fichas_en_raya = 0
            #Paso suma a las coordenadas del elemento en el que nos encontramos, un número entre 0 y fichas_para_ganar, lo necesario para ver si hay tres en raya
            for paso in range(fichas_para_ganar):
                #Guardamos el elemento actual, en este caso es (fila_inicio+paso) porque comprobamos la diagonal principal
                elemento = tablero[fila_inicio + paso][col_inicio + paso]
                #Si en la posición no hay un espacio, miramos qué elemento es; si hay un espacio, reiniciamos la racha
                if elemento != " ":
                    if elemento == simbolo:
                        # Si el elemento es el mismo que había en la posición anterior, sumamos a la racha
                        fichas_en_raya += 1
                    else:
                        #Si el elemento es distinto al de la posición anterior, establecemos racha en 1 y nos guardamos el valor como <símbolo>
                        simbolo = elemento
                        fichas_en_raya = 1
                    # En caso de que la racha sea igual a fichas_para_ganar, devuelve True (indica que la partida debe acabar) y el símbolo del ganador, para imprimirlo en consola
                    if fichas_en_raya == fichas_para_ganar:
                        return True, simbolo
                else:
                    #Si hay un espacio, reiniciamos la racha y el símbolo
                    simbolo = None
                    fichas_en_raya = 0

    # =========================================
    # CASO DE VICTORIA POR DIAGONAL SECUNDARIA:
    # =========================================
    #Iniciamos en una fila, y dentro de esa fila vamos creando diagonales del tamaño fichas_para_ganar por cada columna
    for fila_inicio in range(fichas_para_ganar - 1, filas):
        for col_inicio in range(columnas - fichas_para_ganar + 1):
            #Simbolo guarda el símbolo encontrado al recorrer el tablero, normalmente el de la posición (i - 1) para poder compararlo con la posición actual y ver si hay racha o no
            simbolo = None
            #Fichas_en_raya guarda la racha de símbolos iguales seguidos
            fichas_en_raya = 0
            #Paso suma a las coordenadas del elemento en el que nos encontramos, un número entre 0 y fichas_para_ganar, lo necesario para ver si hay tres en raya
            for paso in range(fichas_para_ganar):
                #Guardamos el elemento actual, en este caso es (fila_inicio-paso) porque comprobamos la diagonal inversa
                elemento = tablero[fila_inicio - paso][col_inicio + paso]
                #Si en la posición no hay un espacio, miramos qué elemento es; si hay un espacio, reiniciamos la racha
                if elemento != " ":
                    if elemento == simbolo:
                        # Si el elemento es el mismo que había en la posición anterior, sumamos a la racha
                        fichas_en_raya += 1
                    else:
                        #Si el elemento es distinto al de la posición anterior, establecemos racha en 1 y nos guardamos el valor como <símbolo>
                        simbolo = elemento
                        fichas_en_raya = 1
                    # En caso de que la racha sea igual a fichas_para_ganar, devuelve True (indica que la partida debe acabar) y el símbolo del ganador, para imprimirlo en consola
                    if fichas_en_raya == fichas_para_ganar:
                        return True, simbolo
                else:
                    #Si hay un espacio, reiniciamos la racha y el símbolo
                    simbolo = None
                    fichas_en_raya = 0
    # Si se recorre el tablero entero y no encuentra tres en raya devuelve Falso y no retorna simbolo del ganador
    return False, None



#Función que comprueba si quedan espacios libres en el tablero
def ComprobarTableroLleno():
    #Contador de filas llenas, por cada fila llena este aumenta 1
    filas_llenas = 0
    #Recorro el tablero, guardándome la las filas (estas son listas)
    for fila in tablero:
        #Si en la lista no hay espacios, aumento filas_llenas
        if " " not in fila:
            filas_llenas += 1
    #Si filas_llenas es igual a la cantidad de filas que tiene el tablero devuelve True, que indíca que el tablero está lleno
    if filas_llenas == len(tablero):
        return True
    else:
        #Devuelve false si el tablero aún tiene espacios, para que el juego siga en el flujo normal
        return False


#Función que pide posición al usuario
def PedirPosicion():
    #Posición válida me permite seguir pidiendo posiciones hasta comprobar que sea valida en ValidarPosicion()
    PosValida = False
    while not PosValida:
        #Pido la fila y la columna
        PosFila = (int(input("Introduce la fila: ")) - 1)
        PosColumna = (int(input("Introduce la columna: ")) - 1)
        #Compruebo si la posición es valida con la función ValidarPosicion()
        PosValida = ValidarPosicion(PosFila, PosColumna)
        if not PosValida:
            #Si no es valida pido al usuario que introduzca una posición de nuevo
            print("Posición no válida. Intentalo de nuevo.")
            ImprimirTablero()
    #Devuelvo los valores de la posición de la fila y la posición de la columna (índices para la matriz tablero)
    return PosFila, PosColumna



#Función que genera posición aleatoria, mismo funcionamiento que la función anterior pero haciendo uso de random en vez de inputs
def GenerarPosicionesRandom():
    PosValida = False
    while not PosValida:
        PosFila = random.randint(0, len(tablero) - 1)
        PosColumna = random.randint(0, len(tablero[PosFila]) - 1)
        PosValida = ValidarPosicion(PosFila, PosColumna)
    return PosFila, PosColumna



#Función ValidarPosicion, recibe las coordenadas de una de las dos funciones anteriores
def ValidarPosicion(PosFila, PosColumna):
    #Primero comprueba que las coordenadas estén en los límites de la matriz
    if PosFila < 0 or PosFila >= len(tablero):
        return False
    if PosColumna < 0 or PosColumna >= len(tablero[0]):
        return False
    #Segundo comprueba que haya un espacio en esas mismas coordenadas (que no haya una ficha ya)
    if tablero[PosFila][PosColumna] != " ":
        return False
    #Si ninguna de las condiciones anteriores se ha dado, la posición es válida y devuelve True
    return True



#Función en caso de que se haya elegido el modo de juego Jugador Contra Jugador
def JugadorContraJugador():
    #Creo las variables de control
    acabar_partida = False
    turno_de_juego = 0
    #Bucle de juego, toda la partida transcurre aquí
    while not acabar_partida:
        ImprimirTablero()
        if turno_de_juego % 2 == 0:
            # Jugador 1 (x) juega en turnos pares
            #Pido la posición con la función PedirPosicion() y guardo la ficha en la posición indicada del tablero
            PosFila, PosColumna = PedirPosicion()
            tablero[PosFila][PosColumna] = "x"
        else:
            # Jugador 2 (o) juega en turnos impares
            #Pido la posición con la función PedirPosicion() y guardo la ficha en la posición indicada del tablero
            PosFila, PosColumna = PedirPosicion()
            tablero[PosFila][PosColumna] = "o"
        #Aumento el turno de juego, muy importante para el flujo
        turno_de_juego += 1
        #Compruebo si hay victoria
        acabar_partida, simbolo_ganador = ComprobarVictoria()

        #Limpio un poco la terminas con 5 filas en blanco
        LimpiarTerminal()

        #Si ha ganado, se imprime el mensaje de victoria
        if acabar_partida:
            print(f"¡Jugador {simbolo_ganador} ha ganado!")
        #Si no ha ganado, comprueba si el tablero está lleno, si es así, acaba partida
        if not acabar_partida and ComprobarTableroLleno():
            print("PARTIDA ACABADA POR FALTA DE ESPACIOS DISPONIBLES")
            acabar_partida = True
    #Imprime el tablero final
    if acabar_partida:
        ImprimirTablero()



#Función en caso de que se haya elegido el modo de juego Jugador Contra Máquina
def JugadorContraMaquina():
    #Creo las variables de control
    acabar_partida = False
    turno_de_juego = 0
    #Bucle de juego, toda la partida transcurre aquí
    while not acabar_partida:
        ImprimirTablero()
        if turno_de_juego % 2 == 0:
            #Jugador 1 (x) juega en turnos pares
            #Pido la posición con la función PedirPosicion() y guardo la ficha en la posición indicada del tablero
            PosFila, PosColumna = PedirPosicion()
            tablero[PosFila][PosColumna] = "x"
        else:
            #Jugador 2 (o/máquina) juega en turnos impares
            #Genero la posición con la función GenerarPosicionesRandom() y guardo la ficha en la posición indicada del tablero
            PosFila, PosColumna = GenerarPosicionesRandom()
            tablero[PosFila][PosColumna] = "o"
        #Aumento el turno de juego, muy importante para el flujo
        turno_de_juego += 1
        #Compruebo si hay victoria
        acabar_partida, simbolo_ganador = ComprobarVictoria()

        #Limpio un poco la terminas con 5 filas en blanco
        LimpiarTerminal()

        #Si ha ganado, se imprime el mensaje de victoria
        if acabar_partida:
            print(f"¡Jugador {simbolo_ganador} ha ganado!")
        #Si no ha ganado, comprueba si el tablero está lleno, si es así, acaba partida
        if not acabar_partida and ComprobarTableroLleno():
            print("PARTIDA ACABADA POR FALTA DE ESPACIOS DISPONIBLES")
            acabar_partida = True
    #Imprime el tablero final
    if acabar_partida:
        ImprimirTablero()



#Función en caso de que se haya elegido el modo de juego Máquina Contra Máquina
def MaquinaContraMaquina():
    #Creo las variables de control
    acabar_partida = False
    turno_de_juego = 0
    #Bucle de juego, toda la partida transcurre aquí
    while not acabar_partida:
        ImprimirTablero()
        if turno_de_juego % 2 == 0:
            #Jugador 1 (x/máquina) juega en turnos pares
            #Genero la posición con la función GenerarPosicionesRandom() y guardo la ficha en la posición indicada del tablero
            PosFila, PosColumna = GenerarPosicionesRandom()
            tablero[PosFila][PosColumna] = "x"
        else:
            #Jugador 2 (o/máquina) juega en turnos impares
            #Genero la posición con la función GenerarPosicionesRandom() y guardo la ficha en la posición indicada del tablero
            PosFila, PosColumna = GenerarPosicionesRandom()
            tablero[PosFila][PosColumna] = "o"
        #Aumento el turno de juego, muy importante para el flujo
        turno_de_juego += 1
        #Compruebo si hay victoria
        acabar_partida, simbolo_ganador = ComprobarVictoria()

        #Limpio un poco la terminas con 5 filas en blanco
        LimpiarTerminal()

        #Si ha ganado, se imprime el mensaje de victoria
        if acabar_partida:
            print(f"¡Jugador {simbolo_ganador} ha ganado!")
        #Si no ha ganado, comprueba si el tablero está lleno, si es así, acaba partida
        if not acabar_partida and ComprobarTableroLleno():
            print("PARTIDA ACABADA POR FALTA DE ESPACIOS DISPONIBLES")
            acabar_partida = True
    #Imprime el tablero final
    if acabar_partida:
        ImprimirTablero()