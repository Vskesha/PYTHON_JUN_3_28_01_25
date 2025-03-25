import turtle

wn = turtle.Screen()
t = turtle.Turtle()

user_fullname = wn.textinput("Введення", "Введіть Ваше ім'я та прізвище: ")
user_favorite_color = wn.textinput("Введення", "Введи свій улюблений колір англійською:")
t.color(user_favorite_color)
t.write(user_fullname.title(), font=("Courier", 18, "bold"))

wn.mainloop()
