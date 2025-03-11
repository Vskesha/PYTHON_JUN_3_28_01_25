import turtle

wn = turtle.Screen()
t = turtle.Turtle()

user_fullname = wn.textinput("Введення", "Введіть Ваше ім'я та прізвище")
t.write(user_fullname.title(), font=("Courier", 18, "bold"))

wn.mainloop()
