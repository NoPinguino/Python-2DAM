class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre


p = Persona("Misael")

print(p.__nombre)  # ❌ Error: can't access directly
print(p._Persona__nombre)  # ✅ "Misael"
