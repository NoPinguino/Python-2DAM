frutas = ["pera","pera","manzana","pera","cereza","sandia","piña","manzana"]
frutas.sort()
frutas_encontradas = []
frutasNoDup = []

for i in frutas:
    contador = 0
    if i not in frutas_encontradas:
        for j in frutas:
            if i == j:
                contador+=1
        frutasNoDup.append((i, contador))
        frutas_encontradas.append(i)

max_fruta = frutasNoDup[0][0]
max_cant = frutasNoDup[0][1]

for i in range(len(frutasNoDup)):
    if frutasNoDup[i][1] > max_cant:
        max_fruta = frutasNoDup[i][0]
        max_cant = frutasNoDup[i][1]

print(f"La fruta más popular es <{max_fruta}> encontrada {max_cant} veces.")