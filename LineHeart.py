import turtle
import math
import random
screen  = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor("black")
t.speed(0.01)
t.hideturtle()
t.pensize(1)
colors = ["red", "orange","lime", "yellow", "cyan", "green", "magenta", "blue", "purple"]
for i in range(120):
    t.penup()
    t.goto(0,40)
    angle = i * (math.pi *2) /120
    x =16 * (math.sin(angle) ** 3) * 15
    y = (13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle)) * 15
    c = random.choice(colors)
    t.color(c)
    t.pendown()
    t.goto(x,y)
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)
turtle.done()