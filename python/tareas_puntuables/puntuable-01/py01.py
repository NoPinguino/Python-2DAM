num = int(input("Introduce un entero a calcular los divisores: "))
for i in range(num):
    i = i + 1
    if num % i == 0:
        print(i,end=" ")