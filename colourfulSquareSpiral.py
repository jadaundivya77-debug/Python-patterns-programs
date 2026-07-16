import turtle as t

colors = ["red", "blue", "green", "purple", "orange"]

t.speed(0)
t.hideturtle()

for i in range(150):
    t.pencolor(colors[i % 5])
    t.bgcolor("black")
    t.forward(i * 2)
    t.left(91)

t.done()