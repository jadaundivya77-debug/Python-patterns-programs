import turtle as t

t.speed(0.2)
t.color("cyan")
t.bgcolor("black")
t.hideturtle()

for i in range(8):
    t.forward(100)
    t.backward(100)
    t.left(45)

t.done()