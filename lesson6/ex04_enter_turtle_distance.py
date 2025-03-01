import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

distance = screen.textinput(
    "Distance input", 
    "Введи відстань, яку повинна пройти черепашка: "
)

if distance.isdigit():
    distance = int(distance)
else:
    t.write("Ви ввели не число!", font=("Arial", 18, "normal"), align="center")
    turtle.done()

if distance < 50:
    t.speed(1)
elif distance > 100:
    t.speed(3)
else:
    t.speed(2)

t.forward(distance)

turtle.done()
