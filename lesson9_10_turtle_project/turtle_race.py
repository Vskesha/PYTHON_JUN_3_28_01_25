import turtle

# Настройки програми
fwidth = 800
fheight = 600
border = 20
colors = ["red", "blue", "green", "black", "yellow", "orange", "purple", "brown"]
#--------------------------------------------------------------------------------
hwidth = fwidth // 2
hheight = fheight // 2

finish = hheight - border * 2
start = -finish
# -------------------------------------------------------------------------------

screen = turtle.Screen()
screen.title("Черепаші перегони")
screen.bgcolor("lightblue")
screen.setup(width=fwidth + border * 2, height=fheight + border * 2)


# Функція для початку гри
def start_game(x, y):
    screen.clear()
    t = turtle.Turtle()
    t.hideturtle()
    t.write("Гра розпочалася", font=("Arial", 30, "bold"), align="center")

    initialize_field()
    
# Функція для малювання кнопки "Почати гру"
def draw_start_button():
    w = 200
    h = 50
    t = turtle.Turtle()
    t.penup()
    t.goto(-w // 2, 0)
    t.pendown()
    t.color("black", "green")
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

    t.forward(w // 2)
    t.color("white")
    t.write("Почати гру", font=("Arial", h // 2, "bold"), align="center")
    t.hideturtle()

def initialize_field():
    screen.clear()
    t = turtle.Turtle()
    t.penup()
    t.goto(-hwidth, -hheight)
    t.pendown()
    
    t.pensize(3)
    for _ in range(2):
        t.forward(fwidth)
        t.left(90)
        t.forward(fheight)
        t.left(90)

    t.penup()
    t.goto(-hwidth, start)
    t.pendown()
    t.color("blue")
    t.write("Start", font=("Arial", 14, "bold"))
    t.forward(fwidth)

    t.penup()
    t.goto(-hwidth, finish)
    t.pendown()
    t.color("red")
    t.write("Finish", font=("Arial", 14, "bold"))
    t.forward(fwidth)

# Відслідковування натискання на кнопку
draw_start_button()
screen.onscreenclick(start_game)


turtle.done()
