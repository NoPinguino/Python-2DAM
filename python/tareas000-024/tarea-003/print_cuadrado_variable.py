x = int(input("Introduce el ancho del cuadrilatero: "))
y = int(input("Introduce la altura del cuadrilatero: "))
char = input("Introduce el caracter de relleno: ")
for i in range(x):
    for j in range(y):
        print(char,end="")
    print(" ")
