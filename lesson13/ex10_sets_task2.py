# ----------------------------------
# Завдання 2
# 
# Створіть множину з назвами різних фруктів: 
# "apple", "banana", "cherry". Додайте 
# до множини "orange" і видаліть "banana" 
# за допомогою методу discard(). 
# Виведіть результуючу множину.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.discard("banana")
print(fruits)
