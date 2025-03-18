import turtle

t = turtle.Turtle()
t.shape("circle")

size = 2
t.shapesize(size)
t.penup()

colors = ["red", "blue", "green", "yellow", "purple"]

for i in range(5):
    t.color(colors[i])
    t.goto(i * 20 * size, 0)
    t.stamp()

turtle.done()
