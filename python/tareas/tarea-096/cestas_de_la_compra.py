catalogo = {"pan": 1.2, "leche": 1.5, "huevos": 2.3, "arroz": 1.1}
cestas = {}
cant_cestas = int(input("Cantidad de cestas: "))

for i in range(1, cant_cestas + 1):
    id_cesta = f"cesta_{i}"
    cestas[
        id_cesta
    ] = {}  # En la posición de cestas con clave id_cesta creamos un diccionario
    seguir = True
    while seguir:
        print(f"\n¿Seguir modificando {id_cesta}? [y/n]")
        if input().lower() == "y":
            # Imprime catálogo
            print("\nProductos disponibles:")
            for prod, precio in catalogo.items():
                print(f" - {prod}: {precio}€")
            # Pedir prod y cant y añadir a cesta
            prod_add = input("\n¿Qué producto vas a comprar? ")
            if prod_add not in catalogo:
                print("Ese producto no existe.")
            cant_add = int(input(f"¿Cuántos {prod_add} vas a comprar? "))
            if prod_add in cestas[id_cesta]:
                cestas[id_cesta][prod_add] += cant_add
            else:
                cestas[id_cesta][prod_add] = cant_add
        else:
            print(f"Cesta {id_cesta} cerrada.")
            seguir = False

# Imprimir resultado final
print()
print("Resultado final de las cestas:")
for nombre_cesta, contenido_cesta in cestas.items():
    print(f"Productos en {nombre_cesta}")
    for prod, cant in contenido_cesta.items():
        print(f"{prod} : {cant}")
    print()  # salto de linea entre cestas
