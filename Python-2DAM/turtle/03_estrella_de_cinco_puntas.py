import turtle as t

ventana = t.Screen()
ventana.bgcolor("gray")

cursor = t.Turtle()
cursor.pensize(10)
cursor.color("blue")

cursor.left(108)

for i in range(5):
    cursor.forward(200)
    cursor.left(144)

ventana.mainloop()
