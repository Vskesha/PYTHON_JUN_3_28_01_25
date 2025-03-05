import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

temperature = screen.textinput(
    "Temperature input", 
    "Введіть поточну температуру в °C: "
)

if temperature.isdigit():
    temperature = int(temperature)
else:
    t.color("red")
    t.write(
        "Ви ввели не число!",
        font=("Arial", 18, "normal"),
        align="center",
    )
    turtle.done()

if temperature < 10:
    t.color("blue")
elif temperature <= 25:
    t.color("green")
else:
    t.color("red")

t.forward(100)

turtle.done()
