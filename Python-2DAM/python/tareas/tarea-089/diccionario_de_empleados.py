empleados = {
    "12345678A": {
        "nombre": "Ana López",
        "puesto": "Desarrolladora",
        "sueldo": 28000
    },
    "87654321B": {
        "nombre": "Carlos Pérez",
        "puesto": "Diseñador",
        "sueldo": 25000
    },
    "11223344C": {
        "nombre": "María Gómez",
        "puesto": "Project Manager",
        "sueldo": 32000
    }
}

for k in empleados.keys():
    print(f"Empleado: {empleados.get(k).get('nombre')}")