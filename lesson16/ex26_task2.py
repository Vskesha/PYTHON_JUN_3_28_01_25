# Завдання 2. Дано дві сторони трикутника a і b 
# та кут між ними θ. Потрібно обчислити третю сторону 
# трикутника c за теоремою косинусів. 
# Теорема косинусів: c² = a² + b² - 2·a·b·cos(θ)

import math

def calculate_third_side(a, b, degrees):
    radians = math.radians(degrees)
    # Теорема косинусів: c² = a² + b² - 2·a·b·cos(θ)
    c_squared = a**2 + b**2 - 2 * a * b * math.cos(radians)
    c = math.sqrt(c_squared)
    return c


a = 5
b = 7
angle = 60

c = calculate_third_side(a, b, angle)
print(f"Третя сторона трикутника рівна: {c}")
