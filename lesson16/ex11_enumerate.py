words = ["apple", "banana", "cherry"]
for index, word in enumerate(words):
    print(index, word)

words = ["apple", "banana", "cherry"]
for index, word in enumerate(words, 101):
    print(index, word)
