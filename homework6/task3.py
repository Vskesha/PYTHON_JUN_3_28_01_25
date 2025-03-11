import turtle
import random

screen = turtle.Screen()
screen.setup(width=800, height=600)
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.goto(-380, 0)

step = 50

# Тут код для генерації перешкод

game_over = False
while not game_over and t.xcor() < 400:
    direction = screen.textinput("Direction", "Set direction (up or down or forward): ")
    
    if direction:
        direction = direction.lower().strip()

    if direction == "up":
        t.left(90)
        t.forward(step)
        t.right(90)
    elif direction == "down":
        t.right(90)
        t.forward(step)
        t.left(90)
    t.forward(step)

    # Тут код для перевірки зіткнення

if not game_over:
    pen = turtle.Turtle()
    pen.color("green")
    pen.write("Congratulations! You won!", font=("Arial", 24, "bold"), align="center")

turtle.done()
