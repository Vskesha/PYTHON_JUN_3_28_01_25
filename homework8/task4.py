import turtle

t = turtle.Turtle()
screen = t.getscreen()
screen.bgcolor("darkgrey")
t.penup()
t.shape("turtle")
t.shapesize(4)
t.color("light blue")

while True:
    t.clear()
    command = screen.textinput("Input", "Введи напрямок (вверх, вниз, вліво, вправо)): ").lower().strip()
    distance = screen.textinput("Input", "Введи відстань: ")
    if distance.isdigit():
        distance = int(distance)
    else:
        t.write("Невірна відстань. Введіть число.", font=("Arial", 18, "bold"), align="center")
        continue
    
    if command == "вверх":
        t.sety(t.ycor() + distance)
    elif command == "вниз":
        t.sety(t.ycor() - distance)
    elif command == "вліво":
        t.setx(t.xcor() - distance)
    elif command == "вправо":
        t.setx(t.xcor() + distance)
    else:
        t.write(
            "Невірний напрямок. Можливі напрямки: вверх, вниз, вліво, вправо.",
            font=("Arial", 18, "bold"),
            align="center",
        )

turtle.done()
