import random

jugadores = []
# Diccionario con las palabras y categorías
diccionario_palabras = {
    # ============ CELEBRIDADES ============
    "messi": ("Lionel Messi", "Celebridades"),
    "taylor_swift": ("Taylor Swift", "Celebridades"),
    "elon_musk": ("Elon Musk", "Celebridades"),
    "zendaya": ("Zendaya", "Celebridades"),
    "brad_pitt": ("Brad Pitt", "Celebridades"),
    "rihanna": ("Rihanna", "Celebridades"),
    "shakira": ("Shakira", "Celebridades"),
    "leonardo_dicaprio": ("Leonardo DiCaprio", "Celebridades"),
    "cristiano_ronaldo": ("Cristiano Ronaldo", "Celebridades"),
    "bad_bunny": ("Bad Bunny", "Celebridades"),
    "rosalia": ("Rosalía", "Celebridades"),
    "michael_jordan": ("Michael Jordan", "Celebridades"),
    "beyonce": ("Beyoncé", "Celebridades"),
    "tom_hanks": ("Tom Hanks", "Celebridades"),
    "billie_eilish": ("Billie Eilish", "Celebridades"),
    "scarlett_johansson": ("Scarlett Johansson", "Celebridades"),
    "will_smith": ("Will Smith", "Celebridades"),
    "ariana_grande": ("Ariana Grande", "Celebridades"),
    # ============ LUGARES ============
    "paris": ("París", "Lugares"),
    "madrid": ("Madrid", "Lugares"),
    "tokyo": ("Tokio", "Lugares"),
    "nueva_york": ("Nueva York", "Lugares"),
    "roma": ("Roma", "Lugares"),
    "londres": ("Londres", "Lugares"),
    "barcelona": ("Barcelona", "Lugares"),
    "berlin": ("Berlín", "Lugares"),
    "dubai": ("Dubái", "Lugares"),
    "moscu": ("Moscú", "Lugares"),
    "rio_de_janeiro": ("Río de Janeiro", "Lugares"),
    "sidney": ("Sídney", "Lugares"),
    "amsterdam": ("Ámsterdam", "Lugares"),
    "estambul": ("Estambul", "Lugares"),
    "las_vegas": ("Las Vegas", "Lugares"),
    "venecia": ("Venecia", "Lugares"),
    "cairo": ("El Cairo", "Lugares"),
    "praga": ("Praga", "Lugares"),
    # ============ INFORMATICA / PROGRAMACION ============
    "python": ("Python", "Informatica/Programacion"),
    "java": ("Java", "Informatica/Programacion"),
    "algoritmo": ("Algoritmo", "Informatica/Programacion"),
    "variable": ("Variable", "Informatica/Programacion"),
    "funcion": ("Función", "Informatica/Programacion"),
    "bucle": ("Bucle", "Informatica/Programacion"),
    "clase": ("Clase", "Informatica/Programacion"),
    "objeto": ("Objeto", "Informatica/Programacion"),
    "base_de_datos": ("Base de datos", "Informatica/Programacion"),
    "inteligencia_artificial": ("Inteligencia artificial", "Informatica/Programacion"),
    "javascript": ("JavaScript", "Informatica/Programacion"),
    "git": ("Git", "Informatica/Programacion"),
    "html": ("HTML", "Informatica/Programacion"),
    "css": ("CSS", "Informatica/Programacion"),
    "api": ("API", "Informatica/Programacion"),
    "servidor": ("Servidor", "Informatica/Programacion"),
    "framework": ("Framework", "Informatica/Programacion"),
    "debugging": ("Debugging", "Informatica/Programacion"),
    "compilador": ("Compilador", "Informatica/Programacion"),
    "arrays": ("Arrays", "Informatica/Programacion"),
    # ============ OBJETOS COTIDIANOS ============
    "telefono": ("Teléfono", "Objetos cotidianos"),
    "mochila": ("Mochila", "Objetos cotidianos"),
    "reloj": ("Reloj", "Objetos cotidianos"),
    "cuaderno": ("Cuaderno", "Objetos cotidianos"),
    "teclado": ("Teclado", "Objetos cotidianos"),
    "raton": ("Ratón", "Objetos cotidianos"),
    "silla": ("Silla", "Objetos cotidianos"),
    "mesa": ("Mesa", "Objetos cotidianos"),
    "cepillo_dientes": ("Cepillo de dientes", "Objetos cotidianos"),
    "paraguas": ("Paraguas", "Objetos cotidianos"),
    "llave": ("Llave", "Objetos cotidianos"),
    "cartera": ("Cartera", "Objetos cotidianos"),
    "gafas": ("Gafas", "Objetos cotidianos"),
    "auriculares": ("Auriculares", "Objetos cotidianos"),
    "botella": ("Botella", "Objetos cotidianos"),
    "lampara": ("Lámpara", "Objetos cotidianos"),
    "espejo": ("Espejo", "Objetos cotidianos"),
    "almohada": ("Almohada", "Objetos cotidianos"),
    # ============ PELICULAS / SERIES ============
    "matrix": ("Matrix", "Peliculas/Series"),
    "breaking_bad": ("Breaking Bad", "Peliculas/Series"),
    "stranger_things": ("Stranger Things", "Peliculas/Series"),
    "game_of_thrones": ("Game of Thrones", "Peliculas/Series"),
    "inception": ("Inception", "Peliculas/Series"),
    "star_wars": ("Star Wars", "Peliculas/Series"),
    "harry_potter": ("Harry Potter", "Peliculas/Series"),
    "the_office": ("The Office", "Peliculas/Series"),
    "titanic": ("Titanic", "Peliculas/Series"),
    "la_casa_de_papel": ("La Casa de Papel", "Peliculas/Series"),
    "friends": ("Friends", "Peliculas/Series"),
    "jurassic_park": ("Jurassic Park", "Peliculas/Series"),
    "el_senor_de_los_anillos": ("El Señor de los Anillos", "Peliculas/Series"),
    "avatar": ("Avatar", "Peliculas/Series"),
    "los_vengadores": ("Los Vengadores", "Peliculas/Series"),
    "the_walking_dead": ("The Walking Dead", "Peliculas/Series"),
    "pulp_fiction": ("Pulp Fiction", "Peliculas/Series"),
    "black_mirror": ("Black Mirror", "Peliculas/Series"),
    # ============ COMIDAS / BEBIDAS ============
    "pizza": ("Pizza", "Comidas/Bebidas"),
    "hamburguesa": ("Hamburguesa", "Comidas/Bebidas"),
    "pasta": ("Pasta", "Comidas/Bebidas"),
    "sushi": ("Sushi", "Comidas/Bebidas"),
    "taco": ("Taco", "Comidas/Bebidas"),
    "cafe": ("Café", "Comidas/Bebidas"),
    "te": ("Té", "Comidas/Bebidas"),
    "refresco": ("Refresco", "Comidas/Bebidas"),
    "paella": ("Paella", "Comidas/Bebidas"),
    "tortilla_espanola": ("Tortilla española", "Comidas/Bebidas"),
    "chocolate": ("Chocolate", "Comidas/Bebidas"),
    "helado": ("Helado", "Comidas/Bebidas"),
    "cerveza": ("Cerveza", "Comidas/Bebidas"),
    "vino": ("Vino", "Comidas/Bebidas"),
    "agua": ("Agua", "Comidas/Bebidas"),
    "ensalada": ("Ensalada", "Comidas/Bebidas"),
    "pollo": ("Pollo", "Comidas/Bebidas"),
    "arroz": ("Arroz", "Comidas/Bebidas"),
    # ============ ANIMALES ============
    "perro": ("Perro", "Animales"),
    "gato": ("Gato", "Animales"),
    "leon": ("León", "Animales"),
    "elefante": ("Elefante", "Animales"),
    "aguila": ("Águila", "Animales"),
    "tiburon": ("Tiburón", "Animales"),
    "delfin": ("Delfín", "Animales"),
    "panda": ("Panda", "Animales"),
    "tigre": ("Tigre", "Animales"),
    "jirafa": ("Jirafa", "Animales"),
    "pinguino": ("Pingüino", "Animales"),
    "koala": ("Koala", "Animales"),
    "serpiente": ("Serpiente", "Animales"),
    "caballo": ("Caballo", "Animales"),
    "lobo": ("Lobo", "Animales"),
    "tortuga": ("Tortuga", "Animales"),
    "ballena": ("Ballena", "Animales"),
    "mono": ("Mono", "Animales"),
    # ============ DEPORTES ============
    "futbol": ("Fútbol", "Deportes"),
    "baloncesto": ("Baloncesto", "Deportes"),
    "tenis": ("Tenis", "Deportes"),
    "natacion": ("Natación", "Deportes"),
    "ciclismo": ("Ciclismo", "Deportes"),
    "boxeo": ("Boxeo", "Deportes"),
    "golf": ("Golf", "Deportes"),
    "voleibol": ("Voleibol", "Deportes"),
    "atletismo": ("Atletismo", "Deportes"),
    "formula_1": ("Fórmula 1", "Deportes"),
    "rugby": ("Rugby", "Deportes"),
    "beisbol": ("Béisbol", "Deportes"),
    "hockey": ("Hockey", "Deportes"),
    "surf": ("Surf", "Deportes"),
    "escalada": ("Escalada", "Deportes"),
    "gimnasia": ("Gimnasia", "Deportes"),
    "esgrima": ("Esgrima", "Deportes"),
    "karate": ("Kárate", "Deportes"),
    # ============ PROFESIONES ============
    "medico": ("Médico", "Profesiones"),
    "profesor": ("Profesor", "Profesiones"),
    "ingeniero": ("Ingeniero", "Profesiones"),
    "abogado": ("Abogado", "Profesiones"),
    "arquitecto": ("Arquitecto", "Profesiones"),
    "cocinero": ("Cocinero", "Profesiones"),
    "policia": ("Policía", "Profesiones"),
    "bombero": ("Bombero", "Profesiones"),
    "enfermero": ("Enfermero", "Profesiones"),
    "programador": ("Programador", "Profesiones"),
    "piloto": ("Piloto", "Profesiones"),
    "astronauta": ("Astronauta", "Profesiones"),
    "fotografo": ("Fotógrafo", "Profesiones"),
    "periodista": ("Periodista", "Profesiones"),
    "dentista": ("Dentista", "Profesiones"),
    "veterinario": ("Veterinario", "Profesiones"),
    "actor": ("Actor", "Profesiones"),
    "musico": ("Músico", "Profesiones"),
    # ============ MARCAS ============
    "apple": ("Apple", "Marcas"),
    "nike": ("Nike", "Marcas"),
    "adidas": ("Adidas", "Marcas"),
    "coca_cola": ("Coca-Cola", "Marcas"),
    "mcdonalds": ("McDonald's", "Marcas"),
    "google": ("Google", "Marcas"),
    "amazon": ("Amazon", "Marcas"),
    "samsung": ("Samsung", "Marcas"),
    "microsoft": ("Microsoft", "Marcas"),
    "netflix": ("Netflix", "Marcas"),
    "spotify": ("Spotify", "Marcas"),
    "playstation": ("PlayStation", "Marcas"),
    "nintendo": ("Nintendo", "Marcas"),
    "tesla": ("Tesla", "Marcas"),
    "starbucks": ("Starbucks", "Marcas"),
    "zara": ("Zara", "Marcas"),
    "ikea": ("IKEA", "Marcas"),
    "lego": ("LEGO", "Marcas"),
    # ============ PAISES ============
    "espana": ("España", "Países"),
    "francia": ("Francia", "Países"),
    "italia": ("Italia", "Países"),
    "alemania": ("Alemania", "Países"),
    "japon": ("Japón", "Países"),
    "china": ("China", "Países"),
    "brasil": ("Brasil", "Países"),
    "mexico": ("México", "Países"),
    "argentina": ("Argentina", "Países"),
    "canada": ("Canadá", "Países"),
    "australia": ("Australia", "Países"),
    "india": ("India", "Países"),
    "rusia": ("Rusia", "Países"),
    "egipto": ("Egipto", "Países"),
    "sudafrica": ("Sudáfrica", "Países"),
    "colombia": ("Colombia", "Países"),
    "peru": ("Perú", "Países"),
    "portugal": ("Portugal", "Países"),
}


def limpiar_consola():
    for i in range(50):
        print("")


# def elegir_facil():
#     print("Se ha cambiado la dificultad a: FÁCIL")


# def elegir_normal():
#     print("Se ha cambiado la dificultad a: NORMAL")


# def elegir_dificil():
#     print("Se ha cambiado la dificultad a: DIFICIL")


def selec_nombre_jugadores(num_jugadores):
    jugadores.clear()  # Elimino los jugadores registrados anteriormente
    nombres_usados = set()  # Más eficiente que las listas

    for i in range(num_jugadores):
        while True:
            # Strip elimina espacios en blanco, para evitar nombres vacios
            nuevo_nombre = input(
                f"Introduce el nombre para el jugador [{i + 1}/{num_jugadores}]: "
            ).strip()
            # Valido el nombre
            if nuevo_nombre == "":
                print("⚠️ - ERROR: El nombre no puede estar vacío.")
            elif nuevo_nombre in nombres_usados:
                print("⚠️ - ERROR: Ya existe un jugador con ese nombre.")
            else:
                break
        # Creo a un jugador con el nombre introducido y datos por defecto
        jugador = {"nombre": nuevo_nombre, "rol": "civil", "vivo": True, "puntos": 0}
        # Añado el jugador a la lista de jugadores y el nombre a la lista de nombres usados
        nombres_usados.add(nuevo_nombre)
        jugadores.append(jugador)


def imprimir_marcador():
    for jugador in jugadores:
        print(f"{jugador['nombre']} => {jugador['puntos']}")
    input("Presiona ENTER para continuar y volver al menú principal.")


def selec_num_jugadores():
    try:
        nuevo = int(input("Introduce el número de jugadores personalizado: "))
    except ValueError:
        print("⚠️ - ERROR: Debes introducir un valor numérico.")
        return 3

    if nuevo < 3:
        print("⚠️ - ERROR: Se necesita mínimo tres jugadores para empezar.")
        return 3
    return nuevo


def selec_num_impostores(num_jugadores):
    try:
        nuevo = int(input("Introduce el número de impostores personalizado: "))
    except ValueError:
        print("⚠️ - ERROR: Debes introducir un valor numérico.")
        return 1

    if nuevo > num_jugadores // 3:
        print(
            "⚠️ - ERROR: El número de impostores no puede ser mayor a la tercera parte de los jugadores, cambia primero el número de jugadores si deseas jugar con más impostores."
        )
        return 1
    return nuevo


def selec_max_rondas(num_impostores):
    try:
        nuevo = int(input("Introduce el número de rondas: "))
    except ValueError:
        print("⚠️ - ERROR: Debes introducir un valor numérico.")
        return num_impostores
    if nuevo < num_impostores:
        print(
            "⚠️ - ERROR: Mínimo se debe poder jugar tantas rondas como impostores haya."
        )
        return num_impostores
    return nuevo


def elegir_impostores(num_impostores):
    asignados = 0
    while asignados < num_impostores:
        jugador = random.choice(jugadores)
        if jugador["rol"] == "civil":
            jugador["rol"] = "impostor"
            asignados += 1


def elegir_palabra():
    claves = list(
        diccionario_palabras.keys()
    )  # Paso el KeySet a lista para poder acceder usando índices
    clave_palabra = claves[random.randint(0, len(claves) - 1)]
    return clave_palabra


def imprimir_roles(clave_palabra):
    for i in range(len(jugadores)):
        jugador = jugadores[i]
        limpiar_consola()
        input(f"{jugador['nombre']}, pulsa ENTER cuando estés listo.")
        print("---------------------")
        print(f"JUGADOR: {jugador['nombre']}")
        if jugador["rol"] == "civil":
            print("- Rol: Civil")
            print(f"- Categoría: {diccionario_palabras[clave_palabra][1]}")
            print(f"- Palabra: {diccionario_palabras[clave_palabra][0]}")
        elif jugador["rol"] == "impostor":
            print("- Rol: Impostor")
            print(f"- Categoría: {diccionario_palabras[clave_palabra][1]}")
        else:
            print("⚠️ - ERROR: Jugador con rol NO válido.")
        print("---------------------")
        input("Pulsa ENTER cuando estés listo")
        limpiar_consola()


def pedir_respuestas(respuestas, ronda, max_rondas):
    respuestas_ronda = {}
    for jugador in jugadores:
        if jugador["vivo"]:
            print(f"Ronda {ronda} / {max_rondas}.")
            print(f"Turno de {jugador['nombre']}")
            input("Presiona ENTER para continuar.")
            if jugador["rol"] == "impostor":
                print("Eres impostor.")
            else:
                print("Eres civil.")
            # Compruebo que no se equivoque e introduzca un espacio vacio
            while True:
                palabra = input("Escribe una palabra o pequeña frase: ")
                if palabra == "":
                    print("⚠️ - ERROR: Por favor, no dejes el input vacío.")
                else:
                    break
            # Clave = Nombre de jugador // Valor = Respuesta dada por el jugador
            respuestas_ronda[jugador["nombre"]] = palabra
            limpiar_consola()
    respuestas.append(respuestas_ronda)


def imprimir_respuestas(respuestas, ronda):
    print("Las respuestas dadas en esta ronda son: ")
    for respuesta in respuestas[ronda - 1].keys():
        print(f"- {respuesta} ha dicho {respuestas[ronda - 1][respuesta]}")


def conseguir_jugadores_vivos():
    vivos = []
    for jugador in jugadores:
        if jugador["vivo"]:
            vivos.append(jugador)
    return vivos


def votaciones():
    # Inicializar votos solo para jugadores vivos
    votos = {}
    for jugador in conseguir_jugadores_vivos():
        votos[jugador["nombre"]] = 0

    # Cada jugador vivo vota
    for jugador in conseguir_jugadores_vivos():
        while True:
            print("")
            print(f"Turno de votar de {jugador['nombre']}.")
            # Imprimo los jugadores vivos:
            print("Lista de jugadores:")
            jug_vivos = conseguir_jugadores_vivos()
            for i, jug_vivo in enumerate(jug_vivos):
                print(f"{i + 1} - {jug_vivo['nombre']}")
            # Pido al usuario que introduzca su voto, control de errores.
            try:
                eleccion_voto = int(input("Introduce el voto: ")) - 1
                # Comprobar rango
                if eleccion_voto < 0 or eleccion_voto >= len(jug_vivos):
                    print("⚠️ - ERROR: No existe ese jugador, vota de nuevo.")
                    continue
                # Comprobar que no se vote a sí mismo
                if jug_vivos[eleccion_voto]["nombre"] == jugador["nombre"]:
                    print("⚠️ - ERROR: No te puedes votar a ti mismo, vota de nuevo.")
                    continue
                # Voto válido
                votos[jug_vivos[eleccion_voto]["nombre"]] += 1
                break
            except ValueError:
                print("⚠️ - ERROR: Debes introducir un valor numérico.")

    # Buscar máximo de votos
    max_votos = max(votos.values())
    a_eliminar = []
    # ALmaceno los jugadores que tengan num_votos == max_votos
    for nombre, num_votos in votos.items():
        if num_votos == max_votos:
            a_eliminar.append(nombre)

    # Elegir jugador a eliminar
    nombre_eliminado = random.choice(a_eliminar)
    # Mensaje en caso de empate
    if len(a_eliminar) > 1:
        print("🍀 - Ha habido un empate, se eliminará un jugador aleatoriamente.")

    # Eliminar jugador
    for jugador in jugadores:
        if jugador["nombre"] == nombre_eliminado:
            jugador["vivo"] = False
            num_civiles, num_impostores = contar_vivos_por_rol()
            print("")
            print(f"💀 - El jugador {nombre_eliminado} ha sido eliminado.")
            if jugador["rol"] == "civil":
                print(f"{nombre_eliminado} era civil.")
            else:
                print(f"{nombre_eliminado} era impostor.")
            print(f"Quedan {num_impostores} impostores.")
            input("Presiona ENTER para continuar.")
            break


def contar_vivos_por_rol():
    civiles = 0
    impostores = 0
    for jugador in jugadores:
        if jugador["vivo"]:
            if jugador["rol"] == "civil":
                civiles += 1
            elif jugador["rol"] == "impostor":
                impostores += 1
    return civiles, impostores


def sumar_puntos_civiles():
    # Sumo un punto a todos los civiles.
    for jugador in jugadores:
        if jugador["rol"] == "civil":
            jugador["puntos"] += 1
            # Sumo un punto extra a los civiles que ganen quedando vivos
            # if jugador["vivo"]:
            #     jugador["puntos"] += 1


def sumar_puntos_impostores():
    # Sumo un punto a todos los impostores.
    for jugador in jugadores:
        if jugador["rol"] == "impostor":
            jugador["puntos"] += 1
            # Sumo dos puntosLo de extra a los impostores que ganen quedando vivos
            # if jugador["vivo"]:
            #     jugador["puntos"] += 2


def sumar_puntos_ronda():
    for jugador in jugadores:
        if jugador["rol"] == "impostor" and jugador["vivo"]:
            jugador["puntos"] += 1


def comprobar_victoria(ronda, max_rondas, palabra):
    civiles, impostores = contar_vivos_por_rol()
    # Caso 1: no quedan impostores
    if impostores == 0:
        sumar_puntos_civiles()
        print("")
        print("🎉 - LOS CIVILES GANAN")
        print("Todos los impostores han sido eliminados.")
        print("El impostor o impostores eran: ")
        for jugador in jugadores:
            if jugador["rol"] == "impostor":
                print(f"- {jugador['nombre']}")
        print(f"La palabra era: {diccionario_palabras[palabra][0]}")
        print("")
        input("Presiona ENTER para continuar y volver al menú principal.")
        return True
    # Caso 2: se acaban las rondas o quedan más impostores que civiles
    if ronda > max_rondas or impostores >= civiles:
        sumar_puntos_impostores()
        print("")
        print("😈 - LOS IMPOSTORES GANAN")
        print("No fueron descubiertos a tiempo.")
        print("El impostor o impostores eran: ")
        for jugador in jugadores:
            if jugador["rol"] == "impostor":
                print(f"- {jugador['nombre']}")
        print(f"La palabra era: {diccionario_palabras[palabra][0]}")
        print("")
        input("Presiona ENTER para continuar y volver al menú principal.")
        return True
    return False


def reiniciar_jugadores():
    for jugador in jugadores:
        jugador["rol"] = "civil"
        jugador["vivo"] = True


def partida(num_impostores, max_rondas):
    limpiar_consola()
    # Caso en el que el usuario no haya registrado los jugadores usando selec_nombre_jugadores
    if len(jugadores) == 0:
        print("⚠️ - ERROR: No hay jugadores registrados.")
        print("Debes introducir los nombres antes de iniciar la partida.")
        input("Pulsa ENTER para volver al menú.")
        return
    # Mostrar información de los jugadores y ajustes
    ronda = 1
    respuestas = []
    print("Los jugadores serán: ")
    for i, jugador in enumerate(jugadores):
        print(f"{i + 1} - {jugador['nombre']}")
    print(f"Habrá {num_impostores} impostores.")
    print(f"El máximo de rondas será: {max_rondas}")
    print("")

    # Cancelar / Iniciar partida
    comenzar = input("¿Desea comenzar partida con estos ajustes? [y/n]: ").lower()
    if comenzar != "y":
        print("⛔ - Partida cancelada. Volviendo al menú.")
        input("Pulsa ENTER para continuar.")
        return

    # Seleccionar roles de los jugadores:
    elegir_impostores(num_impostores)
    clave_palabra = elegir_palabra()

    imprimir_roles(clave_palabra)

    while True:
        limpiar_consola()
        pedir_respuestas(respuestas, ronda, max_rondas)
        imprimir_respuestas(respuestas, ronda)
        input("Presiona ENTER para iniciar las votaciones.")
        votaciones()
        # AQUÍ SE ENCUENTRA LA SUMA DE PUNTOS DE CADA RONDA:
        sumar_puntos_ronda()
        if comprobar_victoria(ronda, max_rondas, clave_palabra):
            reiniciar_jugadores()
            break
        ronda += 1
