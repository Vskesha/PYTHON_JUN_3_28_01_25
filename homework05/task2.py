import turtle

screen = turtle.Screen()
t = turtle.Turtle()

user_color = screen.textinput("Color input", "Enter your favorite color: ")
t.pencolor(user_color)
t.width(10)

t.shape("arrow")
t.forward(200)
t.right(144)

t.shape("turtle")
t.forward(200)
t.right(144)

t.shape("square")
t.forward(200)
t.right(144)

t.shape("circle")
t.forward(200)
t.right(144)

t.shape("triangle")
t.forward(200)
t.right(144)

t.shape("classic")

turtle.done()
