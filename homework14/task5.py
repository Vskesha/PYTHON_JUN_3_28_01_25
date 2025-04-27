"""
Завдання 5.

Оптимізуйте наступний код, щоб він був ефективнішим. Код повинен знайти всі парні числа в діапазоні від 1 до 100.

even_numbers = []
for num in range(1, 101):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)
"""

even_numbers = []
for num in range(2, 101, 2):
    even_numbers.append(num)

print(even_numbers)

# Або

print(list(range(2, 101, 2)))
