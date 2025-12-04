seguir = True

# ID -> NOMBRE, EDAD, CURSO
alumnos = {}
alumnos_added = 0


def limpiar():
    for i in range(5):
        print()


def add():
    global alumnos_added
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    curso = input("Curso: ")
    alumnos[alumnos_added] = [nombre, edad, curso]
    alumnos_added = alumnos_added + 1


def deleteID():
    id_borrar = int(input("Introduce ID a borrar: "))
    del alumnos[id_borrar]


def searchEDAD():
    edad_buscar = int(input("Introduce edad a borrar: "))
    for id, lista in alumnos.items():
        if lista[1] == edad_buscar:
            print(f"{id} : {lista[0]}, {lista[1]}, {lista[2]}")


def printDic():
    for id, lista in alumnos.items():
        print(f"{id} : {lista[0]}, {lista[1]}, {lista[2]}")


def modAlumno():
    id_mod = int(input("Introduce ID a modificar: "))
    if id_mod in alumnos:
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        curso = input("Curso: ")
        alumnos[id_mod] = [nombre, edad, curso]
    else:
        print("ID NO ENCONTRADO")


while seguir:
    limpiar()
    print("0. SALIR.")
    print("1. Añadir alumno.")
    print("2. Borrar por ID.")
    print("3. Buscar por edad.")
    print("4. Imprimir tabla.")
    print("5. Modificar alumno.")
    modo = int(input("-> Elige modo: "))
    match modo:
        case 0:
            seguir = False
        case 1:
            add()
        case 2:
            deleteID()
        case 3:
            searchEDAD()
        case 4:
            printDic()
        case 5:
            modAlumno()
        case _:
            print("ERROR ---> Modo no válido, elige de nuevo.")
