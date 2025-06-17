# Завдання 8. 
# Створіть програму, яка приймає ім'я та прізвище 
# у вигляді змінних, використовує метод capitalize() 
# для кожного з них, а потім об'єднує їх 
# у повне ім'я в одному рядку.


first_name = input("Введіть ваше ім'я: ")
last_name = input("Введіть ваше прізвище: ")

first_name = first_name.capitalize()
last_name = last_name.capitalize()

full_name = first_name + " " + last_name

print(f"Повне ім'я: {full_name}")
