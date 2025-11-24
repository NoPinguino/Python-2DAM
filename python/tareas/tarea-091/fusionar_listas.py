nombres = ["Ana", "Luis", "María", "Jorge", "Elena"]
num_tlf = ["612345678", "698765432", "634567890", "655443322", "622110099"]

diccionario = {}
for i in range(len(nombres)):
    diccionario[nombres[i]] = num_tlf[i]

print(diccionario)