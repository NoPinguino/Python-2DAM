frutas = ["pera","manzana","pera","cereza","ciruela","piña","cereza"]
frutasSinDups = []
for i in frutas:
    if i not in frutasSinDups:
        frutasSinDups.append(i)
print(f"Lista sin duplicados: {frutasSinDups}")