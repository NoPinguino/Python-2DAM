# Clase Padre
class Persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad  # pasa por el setter

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, newEdad):
        if newEdad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = newEdad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."


# Hereda de Persona y posee nuevo atributo (curso)
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)  # llamo al constructor padre
        self.curso = curso

    # Casos de herencia múltiple se usa el nombre de la clase en vez de super()

    def presentarse(self):
        return f"""Hola, me llamo {self.nombre}, tengo {self.edad} años. \n
            y estudio {self.curso}."""


# Hereda de Persona y posee nuevo atributo (asignatura)
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def presentarse(self):
        return f"""Hola, me llamo {self.nombre}, tengo {self.edad} años. \n
            Soy profesor de {self.asignatura}."""
