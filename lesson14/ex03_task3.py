# -----------------------------------
# Завдання 3.
# Перевірити вік для голосування на виборах
# Залежно від віку користувача
# виведи у консоль відповідне повідомлення:
# "Ви маєте право голосу."
# "Ви ще не маєте права голосу."

user_age = input("Введіть ваш вік: ")

if int(user_age) >= 18:
    print("Ви маєте право голосу.")
else:
    print("Ви ще не маєте права голосу.")
