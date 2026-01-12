# ⚠️ COMO NO HACER LAS COSAS ⚠️


class persona:  # Clase con nombre en minúsculas (no PascalCase)
    def __init__(self, nombre, edad):
        self.nombre = nombre  # No encapsulado
        self.edad = edad  # No encapsulado

    def presentarme(self):
        print("Hola me llamo " + self.nombre + " y tengo " + str(self.edad) + " años")

    def cumpleanos(self):
        self.edad += 1  # Acceso directo sin validación


# Uso
p = persona("Misael", -5)  # Edad negativa sin control
p.presentarme()

# Cambios directos sin ningún método
p.nombre = "Wassim"
p.edad = -10  # No hay control de errores
p.presentarme()

# Métodos con nombres poco descriptivos
p1 = persona("Misael", 19)
p1.presentarme()
p1.cumpleanos()
p1.presentarme()

# MALAS PRÁCTICAS MOSTRADAS:
#
# - Clase en minúsculas → persona en lugar de Persona.
# - Convención PEP8: clases en PascalCase.
# - No hay encapsulamiento → los atributos nombre y edad son públicos.
# - Se puede cambiar directamente: p.nombre = "Wassim", p.edad = -10 → rompe las reglas.
# - No hay validación → puedes crear persona("Misael", -5) → edad negativa.
# - Métodos con nombres poco claros → presentarme() y cumpleanos() funcionan, pero no explicitan bien su acción.
# - Concatenación de strings sin f-strings → menos legible:
