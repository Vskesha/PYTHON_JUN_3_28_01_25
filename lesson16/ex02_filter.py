def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))

# even_numbers = []
# for number in numbers:
#     if is_even(number):
#         even_numbers.append(number)

# even_numbers = [number for number in numbers if is_even(number)]

print(even_numbers)
