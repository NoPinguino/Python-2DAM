import random

lista_candidatos = [
    ["Misael", 0],
    ["Javier", 0],
    ["Sergio", 0],
    ["Andrea", 0],
    ["Carlos", 0],
    ["Wassim", 0],
    ["Guillermo", 0],
    ["Hugo", 0],
]
seguir = True
while seguir:
    opcion = input("¿Desea seguir?: [y/n]")
    if opcion == "y":
        voto = random.randint(0, len(lista_candidatos))
        lista_candidatos[voto][1] += 1
    else:
        seguir = False
print(lista_candidatos)
