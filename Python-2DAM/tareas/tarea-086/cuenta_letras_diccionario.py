diccionario = {}
cadena = "hola mundo esto Es UNA cad3na"
cadena=cadena.upper()
for letra in cadena:
    if letra in diccionario:
        diccionario[letra] += 1
    else:
        diccionario[letra] = 1

for i in diccionario.keys():
    print(f"{i}: {diccionario[i]}")