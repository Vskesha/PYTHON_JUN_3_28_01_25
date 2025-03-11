import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")
t.color("red")
t.pensize(20)
t.forward(100)

t.penup()
t.right(90)
t.pendown()

t.shape("circle")
t.color("green")
t.pensize(10)
t.forward(100)

t.penup()
t.right(90)
t.pendown()

t.shape("triangle")
t.color("blue")
t.width(30)
t.forward(100)

turtle.done()
