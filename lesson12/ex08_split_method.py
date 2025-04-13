# str.split(separator, maxsplit)

text = "Hello, world! Welcome to Python."
words = text.split()
print(words)

# Splitting by a specific character
text_with_commas = "apple,banana,cherry"
fruits = text_with_commas.split(",")
print(fruits)

fruits2 = text_with_commas.split(",", 1)
print(fruits2)
