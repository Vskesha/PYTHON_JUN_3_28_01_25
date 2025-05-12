"""
Створіть модуль number_utils.py, який міститиме функції для роботи з числами. 
Функції повинні виконувати наступні операції:
Перевіряти, чи є число простим (is_prime).
Знаходити факторіал числа (factorial).
Генерувати список простих чисел до заданого числа (generate_primes).
У файлі main.py імпортуйте модуль number_utils та використовуйте функції для перевірки чисел.
"""

def is_prime(n: int) -> bool:
    """
    Check if a number is prime. Перевіряє чи число просте.

    Args:
        n (int): The number to check. Число для перевірки.
    Returns:
        bool: True if the number is prime, False otherwise. Повертає True, якщо число просте, інакше False.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number. Визначає факторіал числа.

    Args:
        n (int): The number to calculate the factorial for. Число для обчислення факторіалу.
    Returns:
        int: The factorial of the number. Факторіал числа.
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def generate_primes(limit: int) -> list[int]:
    """
    Generate a list of prime numbers up to a given limit. Генерує список простих чисел до заданого ліміту.

    Args:
        limit (int): The upper limit for generating prime numbers. Ліміт для генерації простих чисел.
    Returns:
        list: A list of prime numbers up to the given limit. Повертає список простих чисел до заданого ліміту.
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes
