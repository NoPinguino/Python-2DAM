tablero = []
iconPlayer1 = "x"
iconPlayer2 = "o"
valid_icon = False

def SeleccionarIconos():
    while not valid_icon:
        selec_icono = input("¿Quieres jugar con iconos personalizados? [y/n]: ").lower()
        if selec_icono == "y":
            iconPlayer1 = input("Introduce un caracter: ")
            iconPlayer2 = input("Introduce un caracter: ")
            ValidarIcono()
        else:
            valid_icon = True
            print("Se usaran los iconos por defecto (x/o).")

def ValidarIcono():
    if len(iconPlayer1) == 1 & len(iconPlayer2) == 1:
        valid_icon = True
    else:
        valid_icon = False

def CrearTablero():
    #Pido al usuario el alto y ancho del tablero:
    alto = int(input("Introduce el alto del tablero: "))
    ancho = int(input("Introduce el ancho del tablero: "))
    #Establezco el tamaño del tablero haciendo uso de bucles:
    for i in range(alto):
        tablero.append([])
        for j in range(ancho):
            tablero[i].append(" ")

def ImprimirTablero():
    #Imprime la cabecera del tablero:
    for i in range(len(tablero[0]) + 1):
        if i == 0:
            print(f"   | ",end="")
        else:
            print(f"{i} | ",end="")
    #Imprime el contenido del tablero:
    contador_filas = 1
    for fila in tablero:
        print(f"\n{"-" * ((len(tablero[0]) + 1) * 4)}")
        print(f" {contador_filas} | ",end="")
        contador_filas+=1
        for elemento in fila:
            print(f"{elemento} | ",end="")

#def ValidarPos(fila, columna):


def JugadorContraJugador():
    CrearTablero()
    ImprimirTablero()

def JugadorContraMaquina():
    CrearTablero()

def MaquinaContraMaquina():
    CrearTablero()