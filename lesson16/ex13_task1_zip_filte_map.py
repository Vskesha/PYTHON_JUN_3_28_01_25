# Завдання 1. Напишіть функцію, яка об'єднує 
# два списки чисел, відфільтровує парні числа 
# та обчислює їхні квадрати. 
# Використовуйте функції zip, filter, та map.

def filter_even_squares(list1, list2):
    combined = []
    for num1, num2 in zip(list1, list2):
        combined.append(num1)
        combined.append(num2)
    even_nums = list(filter(lambda x: x % 2 == 0, combined))
    squared_nums = list(map(lambda x: x * x, even_nums))

    return squared_nums


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result = filter_even_squares(list1, list2)
print(result)
