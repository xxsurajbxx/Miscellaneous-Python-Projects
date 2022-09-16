import turtle


Suraj = turtle.Turtle()
Suraj.speed(0)

radius = 200
diameter = radius * 2
Suraj.color('red', 'red')

Suraj.penup()
Suraj.right(90)
Suraj.forward(radius)
Suraj.left(90)
Suraj.pendown()

Suraj.begin_fill()
Suraj.circle(radius)
Suraj.end_fill()

Suraj.penup()
Suraj.backward(radius)
Suraj.left(90)
Suraj.forward(radius - 20)
Suraj.right(90)
Suraj.pendown()

Suraj.color('white')

for x in range(100):
    Suraj.forward(diameter)
    Suraj.left(169)

turtle.done()
