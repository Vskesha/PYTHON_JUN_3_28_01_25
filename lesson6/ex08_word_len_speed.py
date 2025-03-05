import turtle

screen = turtle.Screen()
t = turtle.Turtle()

word = screen.textinput("Введення", "Введіть слово: ")

if len(word) < 5:
    t.speed(1)
elif len(word) < 10:
    t.speed(3)
else:
    t.speed(5)

t.forward(200)

turtle.done()
