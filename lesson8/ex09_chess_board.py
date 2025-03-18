import turtle

t = turtle.Turtle()
t.shape("square")
t.penup()

colors = ["black", "white"]

for y in range(8):
    for x in range(8):
        t.goto(x * 20 - 80, y * 20 - 80)
        if (x + y) % 2 == 0:
            t.color("black")
        if (x + y) % 2 == 1:
            t.color("white")
        t.stamp()

turtle.done()
