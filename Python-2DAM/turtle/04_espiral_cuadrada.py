import turtle as t

ventana = t.Screen()
ventana.bgcolor("gray")

cursor = t.Turtle()
cursor.pensize(10)
cursor.color("blue")

largo = 10

# while largo >= 0:
#     cursor.forward(largo)
#     cursor.left(90)
#     largo = largo - 10

while largo <= 200:
    cursor.forward(largo)
    cursor.left(90)
    largo += 10

ventana.mainloop()
