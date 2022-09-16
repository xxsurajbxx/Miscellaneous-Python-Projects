import turtle


screen = turtle.Screen()
pen = turtle.Turtle()

screen.bgcolor('black')

pen.hideturtle()
pen.speed(0)
pen.color('white')

additive = 10

while True:
    for x in range(30):
        pen.forward(30 - x)
        pen.right(25 + x)
    pen.right(20)
