numeros = [10, 30, 15, 2, 45, 60, 5, 100, 35]
nums_max = []
for i in range(0,3,1):
    num_max = numeros[0]
    for j in numeros:
        if j not in nums_max:
            if j > num_max:
                num_max = j
    nums_max.append(num_max)
print(f"Los tren números más grandes encontrados son: {nums_max}")