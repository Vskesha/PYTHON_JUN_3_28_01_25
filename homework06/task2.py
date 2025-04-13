import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

night_bg = "dark grey"
day_bg = "light blue"

hour = screen.textinput(
    "Time input", 
    "Введи час доби (годину): "
)
hour = hour.lower().strip()

if hour.isdigit():
    hour = int(hour)
    if hour < 8:
        screen.bgcolor(night_bg)
    elif hour < 20:
        screen.bgcolor(day_bg)
    elif hour < 24:
        screen.bgcolor(night_bg)
    else:
        t.color("red")
        t.write("Невірний час!", font=("Arial", 30, "bold"), align="center")
else:
    t.color("red")
    t.write("Невірний формат часу!", font=("Arial", 30, "bold"), align="center")

turtle.done()
