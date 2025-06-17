"""
Напишіть програму, яка приймає список кутів у градусах 
і обчислює синус, косинус та тангенс для кожного кута. 
Використовуйте функції sin, cos та tan з бібліотеки 
math, перетворюючи градуси в радіани за допомогою 
функції radians.
"""

import math

def calculate_trigonometric_functions(
        degrees: list[float]
    ) -> list[tuple[float, float, float]]:
    """
    Calculates sine, cosine and tangent for 
    each degree in the given list.

    Args:
        degrees (list[float]): List of degrees.

    Returns:
        list[tuple[float, float, float]]: List 
        of tuples, each containing sine, cosine 
        and tangent for a given degree.
    """
    result = []
    for degree in degrees:
        rads = math.radians(degree)
        sine = math.sin(rads)
        cosine = math.cos(rads)
        tangent = math.tan(rads)
        result.append((sine, cosine, tangent))
    
    return result
