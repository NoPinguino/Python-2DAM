compis, newCompis = ["Wassim","Misael","Hugo","Emily","Sergio"], []
while compis:
    minum = compis[0]
    for palabra in compis:
        if palabra < minum:
            minum = palabra
    newCompis.append(minum)
    compis.remove(minum)
print(f"Lista ordenada: {newCompis}")