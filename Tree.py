import turtle
import random
import math
import colorsys

# Screen
screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")
screen.title("Animated Growing Tree")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.left(90)
t.penup()
t.goto(0, -350)
t.pendown()

screen.tracer(0)

frame = 0


def tree(branch_len):
    global frame

    if branch_len < 10:
        hue = (frame * 0.01 + random.random() * 0.2) % 1
        leaf = colorsys.hsv_to_rgb(hue, 1, 1)

        t.dot(8, leaf)
        return

    # Branch color
    t.pensize(branch_len / 10)
    t.pencolor("#8B4513")

    t.forward(branch_len)

    angle = 20 + random.randint(-5, 5)

    t.right(angle)
    tree(branch_len * 0.75)

    t.left(angle * 2)
    tree(branch_len * 0.75)

    t.right(angle)
    t.backward(branch_len)


while True:
    t.clear()

    t.left(90 - t.heading())
    t.penup()
    t.goto(0, -350)
    t.pendown()

    random.seed(5)   # Keeps tree shape stable
    tree(120)

    screen.update()
    frame += 1