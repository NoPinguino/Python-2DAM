colores = ["amarillo","azul","morado","dos","rojo","verde","gris","negro","marrón"]
for i in range((len(colores) - 1),0,-1):
    if len(colores[i]) < 4:
        colores.remove(colores[i])
print(colores)