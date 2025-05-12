"""
Напишіть рекурсивну функцію для обчислення факторіалу числа. 
Порівняйте її з ітеративним варіантом і поясніть, у яких випадках 
краще використовувати рекурсію, а в яких ітерацію. Переконайтеся, 
що ваша функція обробляє граничні випадки правильно.
"""

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
