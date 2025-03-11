# Привіт, світ!
import turtle

window = turtle.Screen()
t = turtle.Turtle()

text = "Hello, world!"

t.penup()
t.goto(-250, 50)
t.pendown()
t.color("red")
t.write(text, font=("Arial", 30, "normal"))

t.penup()
t.goto(-250, 0)
t.pendown()
t.color("black")
t.write(text, font=("Courier", 30, "italic"))

t.penup()
t.goto(-250, -50)
t.pendown()
t.color("green")
t.write(text, font=("TimesNewRoman", 30, "bold"))

window.mainloop()