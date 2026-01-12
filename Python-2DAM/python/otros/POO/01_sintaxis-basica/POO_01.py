# PascalCase en lugar de camelCase
class Persona:
    # Constructor
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad  # pasa por el setter

    @property
    def edad(self):
        return self._edad  # Explicar RecursionError

    @edad.setter
    def edad(self, newEdad):
        if newEdad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = newEdad  # Explicar RecursionError

    def esMayorDeEdad(self):
        return self.edad >= 18

    def saludar(self):
        return f"¡{self.nombre} te saluda!"


# Creo una instancia de Persona
objPersona = Persona("Misael", "de la Morena", 19)

# Pruebo método
print(objPersona.saludar())
if objPersona.esMayorDeEdad():
    print(f"{objPersona.nombre} es mayor de edad.")
else:
    print(f"{objPersona.nombre} NO es mayor de edad.")

# Pruebo Setter / Getter
try:
    nuevo = int(input("Nueva edad: "))
    objPersona.edad = nuevo  # Setter
    print(objPersona.edad)  # Getter
except ValueError as e:
    print(e)
