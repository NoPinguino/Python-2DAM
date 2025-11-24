alumnos = {
    "Wassim": {"nota1": 7.5, "nota2": 8.0, "nota3": 6.5},
    "Juan": {"nota1": 5.0, "nota2": 6.0, "nota3": 7.0},
    "Emily": {"nota1": 9.0, "nota2": 8.5, "nota3": 9.5},
    "Raúl": {"nota1": 4.0, "nota2": 3.5, "nota3": 3.0}
}
mejor = ["", 0]
peor = ["", 10]
for key in alumnos:
    promedio = sum(alumnos[key].values()) / len(alumnos[key].keys())
    if promedio > mejor[1]:
        mejor[0] = key
        mejor[1] = promedio

    if promedio < peor[1]:
        peor[0] = key
        peor[1] = promedio
    print(f"{key}: {promedio:.2f}")

print(mejor)
print(peor)