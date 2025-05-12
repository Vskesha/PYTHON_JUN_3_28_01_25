# Завдання 3. Напишіть програму, яка приймає 
# список чисел і знаходить найбільше та найменше 
# значення. Використовуйте функції max та min.

def find_min_max(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest


numbers = [3, 5, 7, 2, 8]
largest, smallest = find_min_max(numbers)
print(f"Найбільше: {largest}, Найменше: {smallest}")
