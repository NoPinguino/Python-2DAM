import turtle as t

x = t.Turtle()


def arriba():
    x.forward(20)


def abajo():
    x.backward(20)


def izquierda():
    x.left(15)


def derecha():
    x.right(15)


pantalla = t.Screen()
pantalla.listen()
pantalla.onkey(arriba, "Up")
pantalla.onkey(abajo, "Down")
pantalla.onkey(izquierda, "Left")
pantalla.onkey(derecha, "Right")


t.done()
