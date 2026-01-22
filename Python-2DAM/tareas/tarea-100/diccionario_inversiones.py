aficiones = {
    "Guillermo": ["cine", "fútbol", "música"],
    "Sebas": ["ajedrez", "cine"],
    "Misael": ["música", "lectura"],
}
aficiones_reverse = {}
for nombre, aficiones in aficiones.items():
    for aficion in aficiones:
        if aficion not in aficiones_reverse:
            aficiones_reverse[aficion] = [nombre]
        else:
            aficiones_reverse[aficion].append(nombre)
print(aficiones_reverse)
