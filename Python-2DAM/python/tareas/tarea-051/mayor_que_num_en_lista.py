#Defino listas y variables básicas
numeros = [5, 12, 37, 48, 3, 89, 24, 76, 55, 61, 9, 30, 42, 18, 97, 70, 66, 81, 25, 33]
nums_mayores = []
num_max = numeros[0]
user = int(input("Introduce un entero (menor que 100): "))

#Busco los números mayores al input y el número máximo
for i in numeros:
    if i > num_max:
        num_max = i
    if i > user:
        nums_mayores.append(i)
if user > num_max:
    num_max = user

#Algoritmo Burbuja
size_list = len(nums_mayores)
for i in range(size_list - 1):
    for j in range(size_list - 1 - i):
        if nums_mayores[j] > nums_mayores[j+1]:
                nums_mayores[j], nums_mayores[j+1] = nums_mayores[j+1], nums_mayores[j]

#Imprimo resultados
print(nums_mayores)
print(f"El número máximo es: {num_max}")