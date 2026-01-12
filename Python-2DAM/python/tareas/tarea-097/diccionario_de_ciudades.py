paises = {
    "India": ["Mumbai", "Delhi", "Bangalore"],
    "China": ["Shanghai", "Beijing", "Guangzhou"],
    "Estados Unidos": ["Nueva York", "Los Ángeles", "Chicago"],
    "Indonesia": ["Yakarta", "Surabaya", "Bandung"],
    "Pakistán": ["Karachi", "Lahore", "Faisalabad"],
    "Nigeria": ["Lagos", "Kano", "Ibadan"],
    "Brasil": ["São Paulo", "Río de Janeiro", "Brasilia"],
    "Bangladés": ["Daca", "Chittagong", "Khulna"],
    "Rusia": ["Moscú", "San Petersburgo", "Novosibirsk"],
    "México": ["Ciudad de México", "Guadalajara", "Monterrey"],
    "España": ["Madrid", "Barcelona", "Valencia"],
}

opcion = input("¿Va a introducir un pais o ciudad?: ")
input_usr = input("Introduce un pais: ")

if opcion == "pais":
    for pais in paises:
        if pais == input_usr:
            for ciudad in paises[pais]:
                print(ciudad)

elif opcion == "ciudad":
    for pais in paises:
        if input_usr in paises[pais]:
            print(f"{input_usr} pertenece a {pais}.")
else:
    print("Opción invalida.")
