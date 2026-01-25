# PascalCase en lugar de camelCase
class Persona:
    # CONSTRUCTOR
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad  # pasa por el setter

    # --- Getter solo de nombre ---
    @property
    def nombre(self):
        return self.__nombre

    # --- Getter solo de apellido ---
    @property
    def apellido(self):
        return self.__apellido

    # --- Getter y Setter de edad ---
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.__edad = nueva_edad

    # --- MÉTODOS ---
    def esMayorDeEdad(self):
        return self.edad >= 18

    def saludar(self):
        return f"¡{self.nombre} te saluda!"


# -----------------------
# Ejemplo de uso
# -----------------------

# Creo una instancia de Persona
objPersona = Persona("Misael", "de la Morena", 19)

# Uso de getter con decorador para nombre (no existe getter)
# try:
#     objPersona.nombre = "Álex"
# except AttributeError:
#     print("⚠️ ERROR: nombre no dispone de un método setter.")

# Uso de método
print(objPersona.saludar())

# Comprobación de edad
if objPersona.esMayorDeEdad():
    print(f"{objPersona.nombre} es mayor de edad.")
else:
    print(f"{objPersona.nombre} NO es mayor de edad.")

# Prueba del setter/getter de edad
try:
    nueva_edad = int(input("Nueva edad: "))
    objPersona.edad = nueva_edad  # setter
    print(f"La nueva edad de {objPersona.nombre} es {objPersona.edad}")  # getter
except ValueError as e:
    print(e)
