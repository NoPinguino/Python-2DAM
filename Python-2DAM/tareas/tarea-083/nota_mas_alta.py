alumnos = {
    "Misael": 9,
    "Hugo": 8,
    "Emily": 7,
    "Wassim": 10,
    "Juan": 7,
}

primer_alumno = next(iter(alumnos))
maximo = [primer_alumno, alumnos[primer_alumno]]

for alumno in alumnos:
    if alumnos[alumno] > maximo[1]:
        maximo = [alumno, alumnos[alumno]]

print(maximo)