frutas = "pera pera manzana cereza manzana pera plátano".lower()
contador = {}
for fruta in frutas.split(" "):
    if fruta not in contador:
        contador[fruta] = 1
    else:
        contador[fruta] += 1
print(contador)