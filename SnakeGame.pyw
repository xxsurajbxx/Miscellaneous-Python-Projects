import turtle
from tkinter import *
from tkinter import messagebox
from random import choice
from time import sleep
from keyboard import is_pressed


def error_message():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()
    messagebox.showinfo('Error', "Please enter a valid answer")
    window.deiconify()
    window.destroy()
    window.quit()


def snake_game(screen=turtle.Screen()):
    snake = turtle.Turtle()
    food = turtle.Turtle()
    pen = turtle.Turtle()
    score_pen = turtle.Turtle()
    high_score_pen = turtle.Turtle()

    # screen settings
    screen.bgcolor('black')
    screen.tracer(0)
    screen.title("Snake Game by: xxsurajbxx")
    screen.update()

    # food settings
    food.hideturtle()
    food.penup()
    food.shape('square')
    food.color('red')
    food.shapesize(stretch_wid=0.8, stretch_len=0.8)

    # pen settings
    pen.color('white')
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.setpos(-350, -350)
    pen.pendown()

    # draw the arena
    for x in range(4):
        pen.forward(700)
        pen.left(90)
    pen.penup()
    pen.setpos(-350, -350)
    pen.pendown()
    for x in range(28):
        pen.forward(700)
        pen.penup()
        pen.setpos(-350, pen.ycor() + 25)
        pen.pendown()
    pen.right(90)
    for x in range(28):
        pen.forward(700)
        pen.penup()
        pen.setpos(pen.xcor() + 25, 350)
        pen.pendown()
    pen.penup()

    # score pen settings
    score_pen.penup()
    score_pen.color('white')
    score_pen.setpos(0, 350)
    score_pen.hideturtle()
    score_pen.speed(0)

    # snake settings
    snake.penup()
    snake.speed(0)
    snake.shape('square')
    snake.color('white')
    snake.shapesize(stretch_wid=0.9, stretch_len=0.9)
    snake.setpos(snake.xcor() + 12.5, snake.ycor() + 12.5)

    # high score pen settings
    high_score_pen.penup()
    high_score_pen.color('white')
    high_score_pen.hideturtle()
    high_score_pen.speed(0)

    # writing the scores
    high_score_file = open('HighScores(SnakeGame).txt', 'r+')
    score_pen.write(f"your score is: {0}", align="center", font=("Courier", 25, "normal"))
    high_score_pen.setpos(375, 325)
    high_score_pen.write("<<Leaderboard>>", align="left", font=("Courier", 25, "normal"))
    high_score_pen.setpos(450, 150)
    high_score_pen.write(high_score_file.read(), align="left", font=("Courier", 25, "normal"))
    high_score_file.close()

    # setup for game
    dx = 0
    dy = 0
    score = 0
    random_list = []
    segments = []
    for z in range(-350, 350, 25):
        random_list.append(z + 12.5)
    x = choice(random_list)
    y = choice(random_list)
    food.setpos(x, y)
    food.showturtle()
    food_position = [x, y]
    positions = []
    loss = False
    sleep(0.5)

    # main loop
    while loss is False:
        screen.update()
        if (is_pressed('w') or is_pressed('Up')) and dy != -25:
            dx = 0
            dy = 25
        if (is_pressed('a') or is_pressed('Left')) and dx != 25:
            dx = -25
            dy = 0
        if (is_pressed('s') or is_pressed('Down')) and dy != 25:
            dx = 0
            dy = -25
        if (is_pressed('d') or is_pressed('Right')) and dx != -25:
            dx = 25
            dy = 0
        snake.setpos(snake.xcor() + dx, snake.ycor() + dy)
        for x in range(len(segments)):
            segments[x].setpos(positions[x])
            segments[x].showturtle()
        positions.insert(0, [snake.xcor(), snake.ycor()])
        positions = positions[:int((score / 5) + 1)]
        if snake.ycor() > 350 or snake.ycor() < -350 or snake.xcor() > 350 or snake.xcor() < -350:
            snake.hideturtle()
            for segment_ in segments:
                segment_.hideturtle()
            pen.setpos(0, 0)
            pen.write("You Lost", align="center", font=("Courier", 25, "bold"))
            pen.setpos(0, -50)
            pen.write("Feels Bad", align="center", font=("Courier", 25, "bold"))
            sleep(3)
            while True:
                name = screen.textinput('name', 'Enter A Three Letter Name')
                if name is None or len(name) != 3:
                    error_message()
                    continue
                else:
                    loss = True
                    break
        for segment in segments:
            if segment.xcor() == snake.xcor() and segment.ycor() == snake.ycor():
                snake.hideturtle()
                for segment_ in segments:
                    segment_.hideturtle()
                pen.setpos(0, 0)
                pen.write("You Lost", align="center", font=("Courier", 25, "bold"))
                pen.setpos(0, -50)
                pen.write("Feels Bad", align="center", font=("Courier", 25, "bold"))
                sleep(3)
                while True:
                    name = screen.textinput('name', 'Enter A Three Letter Name')
                    if name is None or len(name) != 3:
                        error_message()
                        continue
                    else:
                        loss = True
                        break
        if food_position[0] == snake.xcor() and food_position[1] == snake.ycor():
            food.hideturtle()
            score += 5
            score_pen.clear()
            score_pen.setpos(0, 350)
            score_pen.write(f"Your Score is: {score}", align="center", font=("Courier", 25, "normal"))
            random_list = []
            for z in range(-350, 350, 25):
                random_list.append(z + 12.5)
            x = choice(random_list)
            y = choice(random_list)
            food.setpos(x, y)
            food.showturtle()
            food_position = [x, y]
            new_segment = turtle.Turtle()

            # segment settings
            new_segment.penup()
            new_segment.speed(0)
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.shapesize(stretch_wid=0.9, stretch_len=0.9)
            new_segment.hideturtle()
            segments.append(new_segment)
        sleep(0.1)
    high_scores = []
    high_scores.append(name.upper() + f': {score}')
    with open("HighScores(SnakeGame).txt") as f:
        for line in f.read().splitlines():
            high_scores.append(line)
    #sort the scores
    for x in range(len(high_scores)):
        for y in range(len(high_scores)+x):
            if y < 5:
                if int((high_scores[x])[5:]) > int((high_scores[y])[5:]):
                    temp=high_scores[x]
                    high_scores[x] = high_scores[y]
                    high_scores[y] = temp
    high_score_file = open('HighScores(SnakeGame).txt', 'w')
    high_score_file.truncate()
    for x in range(5):
        high_score_file.write(high_scores[x])
        if x < 4:
            high_score_file.write('\n')
    high_score_file.close()
    #write out the scores
    with open('HighScores(SnakeGame).txt') as f:
        high_score_pen.clear()
        high_score_pen.setpos(375, 325)
        high_score_pen.write("<<Leaderboard>>", align="left", font=("Courier", 25, "normal"))
        high_score_pen.setpos(450, 150)
        high_score_pen.write(f.read(), align="left", font=("Courier", 25, "normal"))
    
    screen.update()
    sleep(3)
snake_game()
