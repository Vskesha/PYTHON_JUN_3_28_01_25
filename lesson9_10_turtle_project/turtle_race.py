import time
import turtle
import random

# Настройки програми
fwidth = 800
fheight = 600
border = 20
colors = ["red", "blue", "green", "gray", "yellow", "orange", "purple", "brown"]
turtles = []
number_of_obstacles = 40
obstacles = []
number_of_boosts = 30
boosts_color = "lightgreen"
boosts = []
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
    screen.clear()
    t = turtle.Turtle()
    t.hideturtle()
    t.write("Гра розпочалася", font=("Arial", 30, "bold"), align="center")

    initialize_field()

    generate_obstacles()

    generate_boosts()

    num_players = get_number_of_players()

    get_turtles(num_players)

    status_pen.clear()
    status_pen.write(
        "Клікни мишкою, щоб почати гонку черепах",
        align="center",
        font=("Arial", 16, "bold"),
    )

    screen.onscreenclick(start_race)

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
    t.write("Start", font=("Arial", 14, "bold"))
    t.forward(fwidth)

    t.penup()
    t.goto(-hwidth, finish)
    t.pendown()
    t.color("red")
    t.write("Finish", font=("Arial", 14, "bold"))
    t.forward(fwidth)

    t.hideturtle()

def get_number_of_players():
    count = screen.numinput(
        "Кількість гравців",
        "Введіть кількість гравців (2-8):",
        minval=2,
        maxval=8,
    )
    return int(count)

def get_turtles(num_players):
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
    turtle.tracer(0)
    game_in_progres = True
    while game_in_progres:
        for bot in turtles:

            for boost in boosts:
                if bot.distance(boost) < 20:
                    bot.setheading(90)
                    bot.forward(random.randint(30, 50))

            direction = 90
            for obs in obstacles:
                if bot.distance(obs) < 20:
                    if bot.xcor() < obs.xcor():
                        direction = 145
                    else:
                        direction = 45
                    break

            bot.setheading(direction)

            bot.forward(random.randint(1, 10))
            if bot.ycor() >= finish:
                game_in_progres = False
                winner = bot
                break

        update_status()
        turtle.update()
        time.sleep(0.15)

    turtle.tracer(1)
    winner_color = winner.color()[0]
    winner.goto(0, 0)
    winner.write(
        f"Переможець: {winner_color}", 
        font=("Arial", 25, "bold"), 
        align="center"
    )
    winner.shapesize(3)
    winner.goto(0, -60)
    
    status_pen.clear()
    
def update_status():
    leading_turtle = turtles[0]
    for turtle in turtles:
        if turtle.ycor() > leading_turtle.ycor():
            leading_turtle = turtle
    
    leader_color = leading_turtle.color()[0]
    
    distance_to_finish = finish - leading_turtle.ycor()
    if distance_to_finish < 0:
        distance_to_finish = 0
    
    status_pen.clear()
    status_pen.write(
        f"Лідирує: {leader_color:<10} Дистанція до фінішу: {int(distance_to_finish):>4}",
        align="center",
        font=("Arial", 16, "bold")
    )

def generate_obstacles():
    for _ in range(number_of_obstacles):
        x = random.randint(-hwidth + border, hwidth - border)
        y = random.randint(start + border, finish - border)
        obs = turtle.Turtle()
        obs.speed(0)
        obs.shape("circle")
        obs.color("black")
        obs.penup()
        obs.goto(x, y)
        obstacles.append(obs)

def generate_boosts():
    for _ in range(number_of_boosts):
        x = random.randint(-hwidth + border, hwidth - border)
        y = random.randint(start + border, finish - border)
        boost = turtle.Turtle()
        boost.speed(0)
        boost.shape("circle")
        boost.color(boosts_color)
        boost.penup()
        boost.goto(x, y)
        boosts.append(boost)

# Відслідковування натискання на кнопку
draw_start_button()
screen.onscreenclick(start_game)


turtle.done()

# Команди для перетворення в .exe файл
# pip install pyinstaller

# Для Windows: pyinstaller --onefile --windowed --icon=turtle2.ico turtle_race.py
# Для macOS: pyinstaller --onefile --windowed --icon=turtle2.icns turtle_race.py
