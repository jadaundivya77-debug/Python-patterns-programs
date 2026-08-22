import turtle

# Screen
screen = turtle.Screen()
screen.bgcolor("gray")
screen.title("Chess Board")

# Turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Settings
size = 60
start_x = -240
start_y = 240

# Draw chessboard
for row in range(8):
    for col in range(8):

        x = start_x + col * size
        y = start_y - row * size

        t.penup()
        t.goto(x, y)
        t.pendown()

        # Alternate black and white
        if (row + col) % 2 == 0:
            t.fillcolor("white")
        else:
            t.fillcolor("black")

        t.begin_fill()

        for _ in range(4):
            t.forward(size)
            t.right(90)

        t.end_fill()

turtle.done()