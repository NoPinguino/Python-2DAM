class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre


p = Persona("Misael")

# print(p.__nombre)  # ERROR
print(
    p._Persona__nombre
)  # ✅ "Misael" -> Python lo lee, pero es mala práctica. Usa getter!!!
