import turtle as t

ventana = t.Screen()
ventana.bgcolor("yellow")

cursor = t.Turtle()
cursor.pensize(10)
cursor.color("red")

cursor.left(45)

for i in range(4):
    cursor.left(90)
    cursor.forward(200)
    cursor.goto(0, 0)

ventana.mainloop()
