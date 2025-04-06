import turtle
import random


# Настройки програми
# -------------------------------------------------------
fwidth = 800
fheight = 600
border = 20
num_players = 2
bot_max_step = 10
colors = ["red", "blue", "green", "gray", "yellow", "orange", "purple", "brown"]
turtles = []
# -------------------------------------------------------
hwidth = fwidth // 2
hheight = fheight // 2
finish = hheight - border * 2
start = -finish
# -------------------------------------------------------

screen = turtle.Screen()
screen.title("Черепаші перегони")
screen.bgcolor("lightblue")
screen.setup(width=fwidth + border * 2, height=fheight + border * 2)

# Функція для початку гри
def start_game(x, y):
    screen.clear()
    t = turtle.Turtle()
    t.write("Hello")

    initialize_field()

    get_number_of_players()

    generate_turtles()

    start_race()


# функція для малюванн кнопки "Почати гру"
def draw_start_button():
    w = 200
    h = 50
    t = turtle.Turtle()
    t.color("black", "green")
    
    t.penup()
    t.goto(-w // 2, 0)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    t.hideturtle()

    t.forward(w // 2)
    t.color("white")
    t.write(
        "Почати гру", 
        font=("Arial", h // 2, "bold"), 
        align="center",
    )

def initialize_field():
    screen.clear()
    t = turtle.Turtle()
    t.speed(5)
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
    t.write("start", font=("Arial", 14, "bold"))
    t.forward(fwidth)

    t.penup()
    t.goto(-hwidth, finish)
    t.pendown()
    t.color("red")
    t.write("finish", font=("Arial", 14, "bold"))
    t.forward(fwidth)

    t.hideturtle()
    
def get_number_of_players():
    global num_players

    user_num = screen.numinput(
        "Кількість черепах",
        "Введи кількість гравців (2 - 8):",
        default=2,
        minval=2,
        maxval=8
    )

    num_players = int(user_num)

def generate_turtles():
    turtles.clear()
    interval = fwidth / (num_players + 1)
    startx = -hwidth + interval

    for i in range(num_players):
        bot = turtle.Turtle()
        bot.shape("turtle")
        bot.color(colors[i])
        bot.penup()
        bot.goto(startx + i * interval, start)
        bot.pendown()
        bot.setheading(90)
        turtles.append(bot)

def start_race():
    game_in_progres = True
    while game_in_progres:
        for bot in turtles:
            bot.forward(random.randint(1, bot_max_step))
            



#--------------------------------------------------
draw_start_button()
screen.onscreenclick(start_game)


turtle.done()
