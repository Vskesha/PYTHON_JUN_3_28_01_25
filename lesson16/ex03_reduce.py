from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)

# total = 0
# for number in numbers:
#     total = add(total, number)

print(total)
