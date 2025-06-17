"""
Створіть функцію, яка приймає список чисел і повертає список з 
квадратами цих чисел. Використовуйте різні типи аргументів, 
такі як позиційні та іменовані аргументи. Переконайтеся, що функція 
працює з будь-якою кількістю аргументів за допомогою *args.
"""

def to_square(*args: int | float) -> list[int | float]:
    """
    Takes one or more numbers and returns a list containing their squares. Отримує один або більше чисел і повертає список з квадратами цих чисел.

    Args:
        *args (int, float): One or more numbers. Одне або більше чисел.

    Returns:
        list: A list of squares of the input numbers. Список з квадратами вхідних чисел.
    """
    squares = []
    for num in args:
        squares.append(num ** 2)
    return squares
