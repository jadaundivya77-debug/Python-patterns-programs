import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.penup()
t.color("#ffb6c1")
for i in range(120):

    angle = i * (2 * math.pi) / 120

    x = 16 * (math.sin(angle) ** 3)
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle))
    
    x *= 15
    y *= 15

    t.goto(x, y)

    t.write(
        "I love Myself",
        align="center",
        font=("Arial", 8, "bold")
    )
turtle.done()

