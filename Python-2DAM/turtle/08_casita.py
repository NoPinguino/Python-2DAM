import turtle as t

cursor = t.Turtle()
cursor.speed(100)

cursor.pensize(10)
cursor.color("red")

for _ in range(4):
    cursor.forward(100)
    cursor.right(90)
for _ in range(3):
    cursor.forward(100)
    cursor.left(120)

t.done()
