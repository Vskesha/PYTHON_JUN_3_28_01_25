import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

number = int(screen.textinput("Distance input", "Введи число: "))

if number > 0:
    t.forward(number)
else:
    t.backward(-number)


turtle.done()
