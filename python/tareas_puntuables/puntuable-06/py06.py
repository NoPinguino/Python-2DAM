palabras = ["sol", "luna", "mar", "estrella", "cielo"]
palabras_new = []
char = "s"
for i in palabras:
    for j in i:
        if j == "s":
            palabras_new.append(i)
        break
print(palabras_new)