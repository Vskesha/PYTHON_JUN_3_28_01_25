names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris", "Tokyo"]

for name, age, city in zip(names, ages, cities):
    print(f"My name is {name}, I am {age} years old and I live in {city}.")
