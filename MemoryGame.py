import turtle
from random import randint
from time import sleep
from sys import exit


def rng():
    randnum1 = str(randint(1, 5))
    randnum2 = str(randint(1, 5))
    randnum3 = str(randint(1, 5))
    randnum4 = str(randint(1, 5))
    num_list = [randnum1, randnum2, randnum3, randnum4]
    return num_list


def check(number_list, screen, pen):
    for number in range(4):
        if number is 0:
            userans = screen.textinput('userans', 'What Was The 1st Number?')
        if number is 1:
            userans = screen.textinput('userans', 'What Was The 2nd Number?')
        if number is 2:
            userans = screen.textinput('userans', 'What Was The 3rd Number?')
        if number is 3:
            userans = screen.textinput('userans', 'What Was The 4th Number?')
        if userans == number_list[number]:
            print('Correct')
            print('Good Job')
            pen.clear()
        else:
            return False


def memory_game(screen):
    screen.bgcolor('black')
    screen.title("Memory Game by: xxsurajbxx")
    peripherals_pen = turtle.Turtle()
    pen = turtle.Turtle()
    pen.penup()
    pen.setpos(0, 0)
    pen.hideturtle()
    pen.color('white')
    peripherals_pen.hideturtle()
    peripherals_pen.color('white')
    peripherals_pen.penup()
    peripherals_pen.setpos(0, 250)
    peripherals_pen.write("Memory Game", align='center', font=('Courier', 50, 'normal'))
    peripherals_pen.setpos(0, 200)
    peripherals_pen.write("By: Suraj Bhardwaj", align='center', font=('Courier', 25, 'normal'))
    for lvl in range(1, 11):
        pen.write(f"lvl {lvl}", align="center", font=("Courier", 50, "normal"))
        sleep(2)
        pen.clear()
        wait = 3 - lvl / 4
        answers = rng()
        for x in range(4):
            pen.write(answers[x], align="center", font=("Courier", 50, "normal"))
            sleep(wait)
            pen.clear()
            sleep(0.5)
        if check(answers, screen, pen) is False:
            pen.write("You Lost", align="center", font=("Courier", 50, "normal"))
            pen.setpos(pen.xcor(), pen.ycor()-50)
            pen.write("Feels Bad", align="center", font=("Courier", 50, "normal"))
            sleep(1)
            exit()
        else:
            pen.write("You Won", align="center", font=("Courier", 50, "normal"))
            sleep(1)
            pen.setpos(pen.xcor(), pen.ycor()-50)
            pen.write("For Now...", align="center", font=("Courier", 50, "normal"))
            sleep(0.75)
            pen.setpos(pen.xcor(), pen.ycor()+50)
            pen.clear()
    pen.write("You Won", align="center", font=("Courier", 50, "normal"))
    pen.setpos(pen.xcor(), pen.ycor()-40)
    pen.write("Congratulations", align="center", font=("Courier", 50, "normal"))
    turtle.done()

