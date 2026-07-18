import turtle as t

t.bgcolor("black")
t.color("yellow")
t.speed(0)
t.hideturtle() 
t.begin_fill()
t.left(140)
t.forward(180)
for i in range(36):
    t.color("red")
    for j in range(2):
        t.circle(100, 60)
        t.left(120)
    t.left(10)
    
   
t.color("yellow")
t.circle(-90, 200)

t.left(120)

t.circle(-90, 200)

for i in range(36):
    t.color("red")
    
    for j in range(2):
        t.circle(100, 60)
        t.left(120)
    t.left(10)
    
t.color("yellow")  

t.forward(180)



t.done()