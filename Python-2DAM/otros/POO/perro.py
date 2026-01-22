class Perro:
    def __init__(self, nombre, raza, edad, sexo):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__sexo = sexo

    @property  # Getter
    def nombre(self):
        return self.__nombre

    @nombre.setter  # Setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property  # Getter
    def raza(self):
        return self.__raza

    @raza.setter  # Setter
    def raza(self, nuevo_raza):
        self.__raza = nuevo_raza

    @property  # Getter
    def edad(self):
        return self.__edad

    @edad.setter  # Setter
    def edad(self, nuevo_edad):
        self.__edad = nuevo_edad

    @property  # Getter
    def sexo(self):
        return self.__sexo

    @sexo.setter  # Setter
    def sexo(self, nuevo_sexo):
        self.__sexo = nuevo_sexo

    def ladrar(self):
        return f"El perro {self.__nombre} hace 'GUAU GUAU'!!!"

    def caminar(self, n_pasos):
        return f"El perro {self.__nombre} ha caminado {n_pasos} pasos."

    def comer(self, comida):
        return f"El perro {self.__nombre} está comiendo {comida}."

    def calcEdadHumano(self):
        return self.__edad * 7


mi_perro = Perro("Tango", "Labrador", 5, "Macho")
print(mi_perro.nombre)

mi_perro.nombre = "Raúl"
print(mi_perro.nombre)

print(mi_perro.comer("Chocolate"))
print(f"El perro {mi_perro.nombre} tiene {mi_perro.calcEdadHumano()} años")
