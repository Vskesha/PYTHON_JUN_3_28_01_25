import turtle

wn = turtle.Screen()
wn.title("Базові команди для руху і малювання")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

t.goto(100, 100)

t.penup()
t.goto(200, 200)

t.pendown()
t.goto(100, -100)

t.backward(200)

wn.mainloop()
