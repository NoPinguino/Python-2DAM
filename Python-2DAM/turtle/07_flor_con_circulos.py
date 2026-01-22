import turtle as t

ventana = t.Screen()

cursor = t.Turtle()
cursor.speed(100)

for _ in range(12):
    cursor.circle(100)
    cursor.left(30)

ventana.mainloop()
