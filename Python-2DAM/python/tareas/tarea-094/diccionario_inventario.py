almacen = {
    "manzanas": 50,
    "naranjas": 30,
    "platanos": 20,
    "peras": 15
}
seguir = True
while seguir:
    print("¿Quieres seguir modificando?: [y/n]")
    if input().lower() == "n":
        seguir = False
    else:
        print("¿Qué producto vas a modificar?: ")
        for prod in almacen:
            print(f"{prod}: {almacen[prod]}")
        prod_modificar = input().lower()
        if prod_modificar in almacen:
            print("¿Qué quieres hacer?")
            print("1. Sacar unidades")
            print("2. Meter unidades")
            mode = int(input())
            if mode == 1:
                cantidad = int(input("¿Cuántas unidades vas a sacar?: "))
                if cantidad < almacen[prod_modificar]:
                    almacen[prod_modificar] -= cantidad
                    print(f"Nueva cantidad de {prod_modificar}: {almacen[prod_modificar]}")
                else:
                    print("Cantidad insuficiente.")
            elif mode == 2:
                cantidad = int(input("¿Cuántas unidades vas a meter?: "))
                almacen[prod_modificar] += cantidad
                print(f"Nueva cantidad de {prod_modificar}: {almacen[prod_modificar]}")
            else:
                print("Error, modo incorrecto.")
print()
for prod in almacen:
    print(f"{prod}: {almacen[prod]}")