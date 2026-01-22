import turtle as t

pantalla = t.Screen()
cursor = t.Turtle()
cursor.hideturtle()

cursor.write("Hola Mundo", align="center", font=("Arial", 30, "italic"))

pantalla.mainloop()
