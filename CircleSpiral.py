import turtle


Suraj = turtle.Turtle()
Suraj.speed(0)
x = 0
for y in range(5000):
    Suraj.forward(x)
    Suraj.left(15)
    x += 0.025
turtle.done()
