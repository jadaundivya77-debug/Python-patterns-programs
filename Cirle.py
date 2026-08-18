import turtle as t
import colorsys

t.bgcolor("black")
t.setpos(-90, 80)

t.tracer(100)
t.pensize(2)
t.hideturtle()

hue = 0.0

for i in range(500):

    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)

    t.fd(200)
    t.rt(91)
    t.circle(50)

    hue += 0.002

t.exitonclick()
