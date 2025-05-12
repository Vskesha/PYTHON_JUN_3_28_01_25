# Завдання 4. Напишіть програму, яка приймає список чисел 
# і перевіряє, чи є всі числа позитивними, та чи є принаймні 
# одне число більше 10. Використовуйте функції all та any.

def check_conditions(numbers):
    all_positive = all(num > 0 for num in numbers)
    any_greater_than_ten = any(num > 10 for num in numbers)
    return all_positive, any_greater_than_ten


numbers = [1, 2, 3, 11, 5]
positive, greater_ten = check_conditions(numbers)
print(f"Всі числа позитивні: {positive}, Є число більше 10: {greater_ten}")
