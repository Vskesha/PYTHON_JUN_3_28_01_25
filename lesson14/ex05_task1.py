# -----------------------------------
# Завдання 1.
# Програма виводить "Ідеальна погода для пікніка!"
# тільки якщо температура перевищує 25 градусів і
# погода сонячна або хмарна. В іншому випадку
# виведи "Можливо, краще залишитися вдома."
# Цей приклад демонструє, як можна
# використовувати and та or разом для
# формування складніших умовних виразів.

temperature = input("Введіть температуру: ")
weather = input("Введіть погоду (сонячно, хмарно, дощ, гроза і т.п.): ")

temperature = int(temperature)

if temperature > 25 and (weather == "сонячно" or weather == "хмарно"):
    print("Ідеальна погода для пікніка!")
else:
    print("Можливо, краще залишитися вдома.")
