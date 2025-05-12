import math

# Перетворення радіан в градуси
print(f"π радіан = {math.degrees(math.pi)}°")
print(f"π/2 радіан = {math.degrees(math.pi / 2)}°")
print(f"2π радіан = {math.degrees(math.pi * 2)}°")
print("-" * 50)

# Перетворення градусів в радіани
print(f"90° = {math.radians(90)} радіан")
print(f"180° = {math.radians(180)} радіан")
print(f"360° = {math.radians(360)} радіан")
print("-" * 50)

# Визначення косинуса та синуса кутів у градусах
print(f"Косинус кута 45° = {math.cos(math.radians(45))}")
print(f"Синус кута 90° = {math.sin(math.radians(90))}")
