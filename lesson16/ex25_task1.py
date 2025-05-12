# Завдання 1. Дано дві сторони трикутника a і b 
# та кут між ними θ. Потрібно обчислити висоту 
# трикутника, проведену до сторони a.

import math

def calculate_height(a, b, theta_degrees):
    theta_radians = math.radians(theta_degrees)

    area = a * b * math.sin(theta_radians) / 2

    height = 2 * area / a

    return height


a = 5
b = 7
angle = 60

height = calculate_height(a, b, angle)
print(f"Висота, проведена до сторони a: {height:.2f}")
