# -----------------------
# Clase Empleado
# -----------------------
class Empleado:
    def __init__(self, nombre, apellido, sueldo, fichado=False):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldo = sueldo
        self.__fichado = fichado

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        self.__sueldo = nuevo_sueldo

    def ficharEntrada(self):
        if not self.__fichado:
            print(f"{self.nombre} ha fichado la entrada.")
            self.__fichado = True
        else:
            print(f"{self.nombre} ya había fichado y se encontraba trabajando.")

    def ficharSalida(self):
        if self.__fichado:
            print(f"{self.nombre} ha fichado la salida.")
            self.__fichado = False
        else:
            print(f"{self.nombre} no había fichado y se encuentra fuera de oficina.")

    # Método genérico trabajar → puede ser polimórfico
    def trabajar(self):
        print(f"{self.nombre} está trabajando (empleado genérico).")


# -----------------------
# Clase Diseñador
# -----------------------
class Disenador(Empleado):
    def __init__(self, nombre, apellido, sueldo, herramientas=None):
        if herramientas is None:
            herramientas = []
        super().__init__(nombre, apellido, sueldo)
        self.__herramientas = herramientas

    @property
    def herramientas(self):
        return self.__herramientas

    @herramientas.setter
    def herramientas(self, nuevas_herramientas):
        self.__herramientas = nuevas_herramientas

    def disenar(self):
        print(f"{self.nombre} está diseñando usando {', '.join(self.__herramientas)}.")

    # Polimorfismo: redefinir trabajar
    def trabajar(self):
        self.disenar()


# -----------------------
# Clase Programador
# -----------------------
class Programador(Empleado):
    def __init__(self, nombre, apellido, sueldo, lenguajes=None):
        if lenguajes is None:
            lenguajes = []
        super().__init__(nombre, apellido, sueldo)
        self.__lenguajes = lenguajes

    @property
    def lenguajes(self):
        return self.__lenguajes

    @lenguajes.setter
    def lenguajes(self, nuevos_lenguajes):
        self.__lenguajes = nuevos_lenguajes

    def programar(self):
        print(f"{self.nombre} está programando en {', '.join(self.__lenguajes)}.")

    # Polimorfismo: redefinir trabajar
    def trabajar(self):
        self.programar()


# -----------------------
# Clase EmpleadoMultifuncional (herencia múltiple)
# -----------------------
class EmpleadoMultifuncional(Programador, Disenador):
    def __init__(self, nombre, apellido, sueldo, lenguajes=None, herramientas=None):
        Programador.__init__(self, nombre, apellido, sueldo, lenguajes)
        Disenador.__init__(self, nombre, apellido, sueldo, herramientas)

    # Polimorfismo: redefinir trabajar → hace todo
    def trabajar(self):
        print(f"{self.nombre} puede programar y diseñar al mismo tiempo:")
        self.programar()
        self.disenar()


# -----------------------
# Función auxiliar
# -----------------------
def salto_de_linea(n):
    for _ in range(n):
        print("")


# -----------------------
# EJEMPLOS DE USO
# -----------------------

# Empleado genérico
empleado = Empleado("Ana", "García", 1800)
empleado.trabajar()  # Polimorfismo: método genérico
salto_de_linea(1)

# Programador
prog = Programador("Luis", "Martínez", 2000, ["Python", "C++"])
prog.trabajar()  # Polimorfismo: llama a programar
salto_de_linea(1)

# Diseñador
dis = Disenador("Laura", "Pérez", 1900, ["Photoshop", "Illustrator"])
dis.trabajar()  # Polimorfismo: llama a disenar
salto_de_linea(1)

# Empleado multifuncional
multi = EmpleadoMultifuncional(
    "Misael",
    "de la Morena",
    2500,
    ["Java", "Python", "JavaScript"],
    ["Jira", "Figma", "Canva"],
)
multi.trabajar()  # Polimorfismo: hace programar + disenar
