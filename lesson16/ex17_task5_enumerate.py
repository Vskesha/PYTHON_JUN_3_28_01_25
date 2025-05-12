# Завдання 5. Напишіть програму, яка приймає 
# список слів і повертає список кортежів, де 
# кожен кортеж містить індекс та слово. 
# Використовуйте функцію enumerate.

def enumerate_words(words):
    enumerated_words = list(enumerate(words))
    return enumerated_words


words = ["apple", "banana", "cherry"]
result = enumerate_words(words)
print(result)
