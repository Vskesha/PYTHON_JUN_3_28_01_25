import turtle
import random

# Настройки програми
fwidth = 800
fheight = 600
border = 20
max_move = 10
colors = ["red", "blue", "green", "black", "yellow", "orange", "purple", "brown"]
turtles = []
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

status_pen = turtle.Turtle()
status_pen.penup()
status_pen.hideturtle()
status_pen.goto(0, finish + border // 2)

# Функція для початку гри
def start_game(x, y):
    screen.onscreenclick(None)

    initialize_field()

    num_players = get_number_of_players()

    generate_turtles(num_players)

    screen.onscreenclick(start_race)
    
# Функція для малювання кнопки "Почати гру"
def draw_start_button():
    w = 200
    h = 50
    t = turtle.Turtle()
    t.speed(8)
    t.penup()
    t.goto(-w // 2, h)
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
    t.speed(10)
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

def get_number_of_players():
    count = screen.numinput(
        "Кількість гравців",
        "Введіть кількість гравців (2-8):",
        minval=2,
        maxval=8,
    )
    return int(count)

def generate_turtles(num_players):
    turtles.clear()
    interval = fwidth // (num_players + 1)
    start_x = -hwidth + interval

    for i in range(num_players):
        bot = turtle.Turtle()
        bot.color(colors[i])
        bot.shape("turtle")
        bot.penup()
        bot.goto(start_x + interval * i, start)
        bot.setheading(90)
        turtles.append(bot)
    
def start_race(x, y):
    screen.onscreenclick(None)
    game_in_progress = True
    while game_in_progress:
        for bot in turtles:
            bot.forward(random.randint(1, max_move))
            if bot.ycor() >= finish:
                game_in_progress = False
                declare_winner(bot)
                break

def declare_winner(winner):
    winner.goto(0, 0)
    winner.write(
        f"Переможець {winner.color()[0]}",
        font=("Arial", 25, "bold"),
        align="center",
    )
    winner.shapesize(3)
    winner.goto(0, -60)


# Відслідковування натискання на кнопку
draw_start_button()
screen.onscreenclick(start_game)


turtle.done()