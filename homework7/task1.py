import turtle

t = turtle.Turtle()
t.shape("turtle")

sides = 6
length = 150
t.color("blue", "grey")
t.begin_fill()
for i in range(sides):
    t.forward(length)
    t.right(360 / sides)
t.end_fill()

t.penup()
t.goto(-250, 200)
t.pendown()

sides = 4
length = 150
t.color("black", "green")
t.begin_fill()
for i in range(sides):
    t.forward(length)
    t.right(360 / sides)
t.end_fill()
t.penup()
t.goto(-250, 200)
t.pendown()

t.penup()
t.goto(150, 50)
t.pendown()

t.color("red", "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

turtle.done()
