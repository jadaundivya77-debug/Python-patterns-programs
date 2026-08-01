import turtle
import math
import colorsys
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("pretty Neon Heart Animation")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.hideturtle()

def heart_x(k):
    return 16 * math.sin(k) ** 3

def heart_y(k):
    return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)
def draw_heart(frame):
    screen.tracer(1)

    for j in range(3):
        t.penup()
        scale = 20+ (j*2)
        t.pensize(5-j)
        hue = (frame * 0.01 + j * 0.15) % 1.0
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.pencolor(color)

        t.penup()

        first = True
        for deg in range(361):
            k = math.radians(deg)

            x = heart_x(k) * scale
            y = heart_y(k) * scale

            if first:
                t.goto(x, y)
                t.pendown()
                first = False
            else:
                t.goto(x, y)

        t.penup()

# Animation loop
frame = 0
while True:
    draw_heart(frame)
    screen.update()
    frame += 1
