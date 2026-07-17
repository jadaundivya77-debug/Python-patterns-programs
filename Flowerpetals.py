import turtle as t

t.speed(0)
t.color("deeppink")
t.bgcolor("black")
t.hideturtle()

for i in range(36):
    for j in range(2):
        t.circle(100, 60)
        t.left(120)
    t.left(10)

t.done()