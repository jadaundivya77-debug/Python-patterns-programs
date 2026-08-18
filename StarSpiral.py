import turtle
import time
turtle.speed(50)
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red", "gold", "purple", "blue"]

for x in range (400):
    turtle.forward(2*x)
    turtle.color(colors[x% 4])
    turtle.left(140)
turtle.done()