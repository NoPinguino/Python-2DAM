import turtle as t

mi_tortuga = t.Turtle()
mi_tortuga.pensize(3)
mi_tortuga.color("green")
mi_tortuga.shape("turtle")
lado = 100

for i in range(3):
    mi_tortuga.forward(lado)
    mi_tortuga.left(120)

t.done()
