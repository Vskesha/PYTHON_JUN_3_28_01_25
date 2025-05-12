"""
Створіть програму, яка використовує глобальну змінну для зберігання 
рахунку гри. Напишіть функції для збільшення, зменшення та скидання 
рахунку. Демонструйте, як використовувати глобальні змінні 
у функціях, і поясніть можливі ризики їх використання.
"""

counter = 0

def increment():
    global counter
    counter += 1

def decrement():
    global counter
    if counter > 0:
        counter -= 1

def reset():
    global counter
    counter = 0
