"""
Напишіть програму, яка обчислює площу та периметр 
правильного многокутника (n-кута), де відомі кількість 
сторін n та довжина однієї сторони s. Використовуйте 
формули S = (n·a²) / (4·tg(π / n)) та P = n·a.
"""

import math


def calculate_area_and_perimeter(n: int, a: float) -> tuple[float, float]:
    """
    Calculates area and perimeter of a regular polygon.

    Args:
        n (int): Number of sides.
        a (float): Length of one side.

    Returns:
        tuple[float, float]: Area and perimeter of the polygon.
    """
    area = n * a**2 / (4 * math.tan(math.pi / n))
    perimeter = n * a
    return area, perimeter
