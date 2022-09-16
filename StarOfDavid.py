import turtle


Suraj = turtle.Turtle()
Suraj.speed(0)
Suraj.penup()
Suraj.backward(100)
Suraj.pendown()
Suraj.color('black', 'cyan')
Suraj.begin_fill()
for x in range(6):
    for y in range(3):
        Suraj.forward(200)
        Suraj.left(120)
    Suraj.forward(100)
    Suraj.right(90)
    Suraj.penup()
    Suraj.forward(50)
    Suraj.left(150)
    Suraj.pendown()
Suraj.end_fill()
turtle.done()
