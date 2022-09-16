import turtle


Suraj = turtle.Turtle()
Suraj.speed(0.3)
x = 0
for y in range(400):
    Suraj.forward(x)
    Suraj.left(45)
    x += 1
turtle.done()
