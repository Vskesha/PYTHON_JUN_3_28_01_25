import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

direction = screen.textinput(
    "Direction input", 
    "Введи напрямок руху (вліво, вправо, вперед, назад): "
)
direction = direction.lower()

if direction == "вліво":
    t.left(90)
    t.forward(100)
elif direction == "вправо":
    t.right(90)
    t.forward(100)
elif direction == "вперед":
    t.forward(100)
elif direction == "назад":
    t.backward(100)
else:
    t.write(
        "Невірний напрямок руху!", font=("TimesNewRoman", 20, "bold"), align="center"
    )


turtle.done()
