# Завдання 3.
# Дано три сторони трикутника a, b і c. 
# Потрібно обчислити кут між сторонами a і b. 
# Теорема косинусів: c² = a² + b² - 2·a·b·cos(θ)

import math

def calculate_angle(a, b, c):
    # Теорема косинусів: c² = a² + b² - 2·a·b·cos(θ)
    # Звідси: 2·a·b·cos(θ) = a² + b² - c²
    # cos(θ) = (a² + b² - c²) / (2·a·b)

    cos_theta = (a**2 + b**2 - c**2) / (2 * a * b)
    theta_radians = math.acos(cos_theta)
    theta_degrees = math.degrees(theta_radians)
    return theta_degrees

a = 5
b = 7
c = 9
print(f"Кут між сторонами a та b: {calculate_angle(a, b, c):.2f}°")
print(f"Кут між сторонами b та c: {calculate_angle(b, c, a):.2f}°")
print(f"Кут між сторонами c та a: {calculate_angle(c, a, b):.2f}°")
