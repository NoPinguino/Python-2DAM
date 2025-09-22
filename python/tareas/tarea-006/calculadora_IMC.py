altura = float(input("Introduce tu altura en CM: "))
altura = altura / 100
peso = float(input("Introduce tu altura en KG: "))
print(f"Tu IMC es de {peso/(altura*altura)}")