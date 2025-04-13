import random
import turtle

t = turtle.Turtle()
t.speed(10)
t.hideturtle()
t.penup()
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"]

for _ in range(25):
    t.color(random.choice(colors))
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()

turtle.done()
