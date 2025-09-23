print("TODAS LAS UNIDADES EN CM")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Rombo")
print("5. Pentágono")
print("6. Hexágono")

fig = int(input("¿De qué figura quieres calcular perímetro y área?"))
match(fig):
    case 1:
        lado = int(input("Introduce el lado: "))
        print(f"Perímetro: {lado * 4}cm")
        print(f"Área: {lado * lado}cm2")

    case 2:
        lado1 = int(input("Introduce el lado 1: "))
        lado2 = int(input("Introduce el lado 2: "))
        print(f"Perímetro: {(lado1 + lado2) * 2}cm")
        print(f"Área: {(lado1 * lado2)}cm2")

    case 3:
        base = int(input("Introduce la base: "))
        altura = int(input("Introduce la altura: "))
        lado = int(input("Introduce el lado: "))
        print(f"Perímetro: {lado * 3}cm")
        print(f"Área: {(base * altura) / 2}cm2")

    case 4:
        diagMay = int(input("Introduce la diagonal mayor: "))
        diagMen = int(input("Introduce la diagonal menor: "))
        lado = int(input("Introduce el lado: "))
        print(f"Perímetro: {lado * 4}cm")
        print(f"Área: {(diagMay * diagMen) / 2}cm2")

    case 5:
        apotema = int(input("Introduce la apotema: "))
        lado = int(input("Introduce el lado: "))
        print(f"Perímetro: {lado * 5}cm")
        print(f"Área: {(lado * 5 * apotema) / 2}cm2")

    case 6:
        lado = int(input("Introduce el lado: "))
        print(f"Perímetro: {lado * 6}cm")
        print(f"Área: {(3 * (3 ** 0.5) * (lado ** 2)) / 2}cm2")