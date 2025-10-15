palabras = ["sol", "luna", "mar", "estrella", "cielo"]
nuevas_palabras = []
char = input("Introduce un caracter: ").lower()
for i in palabras:
    if i.startswith(char):
        nuevas_palabras.append(i)
print(nuevas_palabras)