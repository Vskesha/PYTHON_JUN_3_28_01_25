"""
Напишіть програму, яка приймає список кутів у 
радіанах і обчислює арксинус, арккосинус та 
арктангенс для кожного кута. Використовуйте 
функції asin, acos та atan з бібліотеки math, 
перетворюючи радіани в градуси за допомогою 
функції degrees.
"""

import math

def calculate_trigonometric_functions(
        angles: list[float]
    ) -> list[tuple[float, float, float]]:
    """
    Calculates sine, cosine and tangent for each 
    angle in radians and converts them to degrees.

    Args:
        angles (list[float]): List of angles in radians.

    Returns:
        List of tuples containing sine, cosine 
        and tangent values in degrees.
    """
    results = []
    for angle in angles:
        sine = math.sin(angle)
        cosine = math.cos(angle)
        tangent = math.tan(angle)
        results.append((sine, cosine, tangent))
    return results
