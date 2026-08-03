import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

for i in range(72):
    t.pencolor(colors[i % len(colors)])

    for j in range(6):
        t.circle(80, 60)
        t.left(120)

    t.left(5)

t.hideturtle()
turtle.done()