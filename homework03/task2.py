import turtle

width = 200
height = 150
RIGHT_ANGLE = 90

wn = turtle.Screen()
wn.title("Прямокутник")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")

t.forward(width)
t.right(RIGHT_ANGLE)
t.forward(height)
t.right(RIGHT_ANGLE)
t.forward(width)
t.right(RIGHT_ANGLE)
t.forward(height)
t.right(RIGHT_ANGLE)

wn.mainloop()
