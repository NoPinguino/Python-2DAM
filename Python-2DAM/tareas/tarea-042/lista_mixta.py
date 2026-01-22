mixta = ["manzana","pera","cereza",["perro","gato","león"]]
for i in mixta:
    if isinstance(i, list):
        print(" ")
        for j in i:
            print(j,end=" ")
    else:
        print(i,end=" ")