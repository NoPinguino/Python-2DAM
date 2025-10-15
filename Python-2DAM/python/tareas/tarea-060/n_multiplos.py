num = int(input("Introduce un número entero: "))
cant_mult = int(input("¿Cuántos múltiplos quieres calcular?: ")) + 1
for i in range(1, cant_mult):
    print(f"Múltiplo {i} de {num} = {i * num}")