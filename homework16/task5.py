"""
Напишіть програму, яка приймає довжини двох катетів 
прямокутного трикутника та обчислює довжину гіпотенузи, 
використовуючи теорему Піфагора. Потім обчисліть 
кути між катетами та гіпотенузою.
"""

import math

def calculate_hypotenuse_and_angles(
        a: float, 
        b: float
    ) -> tuple[float, float, float]:
    """
    Calculates hypotenuse and angles between sides.
    Args:
        a (float): Length of the first side.
        b (float): Length of the second side.
    Returns:
        tuple[float, float, float]: Hypotenuse length, 
        angle between sides a and hypotenuse, 
        angle between sides b and hypotenuse.
    """
    hypotenuse = math.sqrt(a**2 + b**2)
    angle_a = math.degrees(math.acos(a / hypotenuse))
    angle_b = math.degrees(math.acos(b / hypotenuse))
    return hypotenuse, angle_a, angle_b
