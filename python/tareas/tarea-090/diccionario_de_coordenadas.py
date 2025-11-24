puntos = {
    "A": (2, 5),
    "B": (0, -3),
    "C": (4, 4),
    "D": (-1, 2),
    "E": (7, 0)
}
maximo = ["",0]
for k in puntos.keys():
    distancia = sum(puntos.get(k))
    if distancia > maximo[1]:
        maximo[0] = k
        maximo[1] = distancia

print(maximo)