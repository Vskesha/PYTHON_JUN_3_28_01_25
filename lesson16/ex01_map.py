def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

# squared_numbers = []
# for number in numbers:
#     sq_number = square(number)
#     squared_numbers.append(sq_number)

# squared_numbers = [square(number) for number in numbers]

print(squared_numbers)
