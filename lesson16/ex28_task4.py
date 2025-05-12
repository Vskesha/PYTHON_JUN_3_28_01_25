# Завдання 4. 
# Напишіть функцію calculate_circle_properties, 
# яка приймає радіус кола і повертає його 
# площу та довжину кола. Використовуйте 
# константу pi з бібліотеки math.
# Формула для площі кола: S = π·r²
# Формула для довжини кола: L = 2·π·r

import math

def calculate_circle_properties(radius):
    circle_area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return circle_area, circumference

r = 5
area, length = calculate_circle_properties(r)
print(f"Площа кола: {area:.2f}")
print(f"Довжина кола: {length:.2f}")
