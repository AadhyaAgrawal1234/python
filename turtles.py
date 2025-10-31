import turtle

t = turtle.Turtle()

t.color("red")
for _ in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(-150, -50)
t.pendown()

t.color("blue")
t.circle(50)

t.penup()
t.goto(100, -50)
t.pendown()

t.color("green")
for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)

turtle.done()
