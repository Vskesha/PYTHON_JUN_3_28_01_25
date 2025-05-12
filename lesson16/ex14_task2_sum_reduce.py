# Завдання 2. Напишіть програму, яка 
# приймає список чисел і обчислює їх 
# суму, середнє значення та добуток.

from functools import reduce

def calculate_aggregates(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    product = reduce(lambda x, y: x * y, numbers)
    return total_sum, average, product


nums = [1, 2, 3, 4, 5]
tot_sum, avg, prod = calculate_aggregates(nums)

print(f"Сума: {tot_sum}, середнє: {avg}, добуток: {prod}")
