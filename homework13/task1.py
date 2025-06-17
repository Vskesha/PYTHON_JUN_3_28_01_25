"""
Завдання 1.
Написати програму, де комп'ютер вибирає випадкове число,
а користувач має його вгадати. Використовуйте умовні
оператори для відгадування числа: виводьте підказки
"занадто велике" або "занадто мале".
"""

import random

max_number = 1_000
random_number = random.randint(1, max_number)

while True:
    user_guess = input(f"Вгадайте число (1 - {max_number:_}): ")

    if not user_guess.isdigit():
        print("Ви ввели не число!")
        continue

    user_guess = int(user_guess)
    if user_guess > random_number:
        print("Занадто велике")
    elif user_guess < random_number:
        print("Занадто мале")
    else:
        print("Ви вгадали!")
        break
