# str.find(substring[, start[, end]]) - знаходить першу позицію
text = "Hello, world! This is a test text that has two words 'world'"

# перша позиція слова "world" в тексті
position = text.find("world")
position = text.index("world")
print(position)

# друга позиція слова "world" в тексті
second_position = text.find("world", position + 1, 50)
print(second_position)

# пошук слова, якого немає в тексті
position = text.find("nonexistent")
# position = text.index("nonexistent")
print(position)  # результат -1, тому слово не знайдено
