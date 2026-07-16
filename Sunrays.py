import turtle as t

t.speed(0)
t.color("orange")
t.hideturtle()

for i in range(72):
    t.forward(150)
    t.backward(150)
    t.bgcolor("black")
    t.left(5)

t.done()