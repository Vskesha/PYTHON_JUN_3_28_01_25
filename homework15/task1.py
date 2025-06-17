"""
Напишіть програму, яка приймає список чисел і обчислює 
квадратний корінь, натуральний логарифм та експоненту 
для кожного числа. Використовуйте функції 
sqrt, log та exp з бібліотеки math.
"""

import math

def calculate_sqrt_log_exp(
        numbers: list[float]
    ) -> list[tuple[float, float, float]]:
    """
    Calculates square root, natural logarithm and 
    exponential for each number in the given list.

    Args:
        numbers (list[float]): List of numbers.

    Returns:
        list: List of tuples containing calculated 
        square root, natural logarithm, and 
        exponential for each number.
    """
    result = []
    for num in numbers:
        if num >= 0:
            sqrt_num = math.sqrt(num)
            log_num = math.log(num)
            exp_num = math.exp(num)
            result.append((sqrt_num, log_num, exp_num))
        else:
            result.append(None)
    return result
