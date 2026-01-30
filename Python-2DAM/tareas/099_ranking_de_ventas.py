ventas = [
    ("Pepe", 200),
    ("Juanito", 150),
    ("Pitingo", 50),
    ("Optimus_Prime", 300),
    ("Pitingo", 50),
    ("Optimus_Prime", 300),
    ("Juanito", 150),
]
diccionario_ventas = {}
for i in range(len(ventas)):
    if ventas[i][0] not in diccionario_ventas:
        diccionario_ventas[ventas[i][0]] = ventas[i][1]
    else:
        diccionario_ventas[ventas[i][0]] += ventas[i][1]

print(diccionario_ventas)
diccionario_ventas = dict(sorted(diccionario_ventas.items(), key=lambda item: item[1]))
print(diccionario_ventas)
