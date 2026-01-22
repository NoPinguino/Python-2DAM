import turtle as t

lados = int(input("Introduce el número de lados: "))
angulo = 360 / lados

ventana = t.Screen()
ventana.bgcolor("gray")

cursor = t.Turtle()
cursor.pensize(10)
cursor.color("blue")

largo = 100

for _ in range(lados):
    t.forward(largo)
    t.left(angulo)

ventana.mainloop()
