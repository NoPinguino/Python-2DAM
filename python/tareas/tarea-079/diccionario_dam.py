alumno1 = ["Misael","de la Morena",19,"2dam"]
alumno2 = ["Hugo","Solis",21,"2dam"]
alumno3 = ["Wassim","Aarab",21,"2dam"]

clase = {
    "idAlumno1": alumno1,
    "idAlumno2": alumno2,
    "idAlumno3": alumno3,
}

for alumno in clase.items():
    print(f"{alumno[0]}: {alumno[1]}")