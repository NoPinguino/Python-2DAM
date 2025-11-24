diccionario = {
    "Matématicas": [5,7,9,4,8],
    "Lengua": [7,8,8,2,10],
    "Historia": [6,9,6,5,7]
}
for v in diccionario.keys():
    prom = sum(diccionario[v])/len(diccionario[v])
    print(f"{v}: {prom}")