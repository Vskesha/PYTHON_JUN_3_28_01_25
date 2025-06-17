"""
Напишіть програму, яка приймає координати двох 
точок на площині та обчислює відстань між ними.
"""

import math

def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculates the distance between two points on a plane.

    Args:
        x1 (float): X coordinate of the first point.
        y1 (float): Y coordinate of the first point.
        x2 (float): X coordinate of the second point.
        y2 (float): Y coordinate of the second point.

    Returns:
        float: The distance between the two points.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
