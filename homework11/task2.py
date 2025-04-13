user_input = input("Введіть число: ")

number = float(user_input)

square = number ** 2

print(f"Квадрат числа: {square}")

separated_digits = " ".join(user_input)
print("Цифри розділені пробілами:", separated_digits)
