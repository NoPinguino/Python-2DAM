class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre


objPersona = Persona("Misael")

# print(p.__nombre)  # ERROR
print(
    objPersona._Persona__nombre
)  # ✅ "Misael" -> Python lo lee, pero es mala práctica. Usa getter!!!
