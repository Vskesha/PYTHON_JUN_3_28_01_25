import turtle

t = turtle.Turtle()
size = 150
font = ("Arial", 20, "bold")

t.color("red")
t.write("Triangle", font=font)
t.begin_fill()
for _ in range(3):
    t.forward(size)
    t.right(120)
t.end_fill()

t.penup()
t.goto(-size, 0)
t.pendown()
t.color("green")
t.write("Square", font=font)
t.begin_fill()
for _ in range(4):
    t.forward(size)
    t.right(90)
t.end_fill()

t.penup()
t.goto(size, 0)
t.color("blue")
t.write("Circle", font=font)
t.goto(size * 3 // 2, -size)
t.pendown()
t.begin_fill()
t.circle(size // 2)
t.end_fill()

t.hideturtle()
turtle.done()
