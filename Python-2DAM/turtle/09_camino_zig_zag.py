import random
import turtle as t

cursor = t.Turtle()
cursor.speed(100)

cursor.pensize(10)
cursor.color("red")

for _ in range(100):
    dir = random.choice(("derecha", "izquierda"))
    if dir == "derecha":
        cursor.forward(100)
        cursor.right(random.randint(0, 361))
    else:
        cursor.forward(100)
        cursor.left(random.randint(0, 361))

t.done()
