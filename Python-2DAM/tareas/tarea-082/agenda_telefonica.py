agenda = {
    "Misael": 555000000,
    "Hugo": 555000001,
    "Alex": 555000002,
    "Wassim": 555000003,
    "Sebas": 555000004,
}
busqueda = input("Introduce un nombre: ")
if busqueda in agenda:
    print(f"Número de {busqueda}: {agenda[busqueda]}")
else:
    print("No se encuentra en la agenda.")