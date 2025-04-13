# str.replace(old, new[, count])
text = "Hello, world!"
print(text)

replaced_text = text.replace("world", "Python")
print(replaced_text)

replaced_text = text.replace("nonexistent", "Python")
print(replaced_text)

# multiple replacements
text = "Hello, world! Hello, everyone!"
print(text)

new_text = text.replace("Hello", "Hi")
print(new_text)

limited_replacement = text.replace("Hello", "Hi", 1)
print(limited_replacement)
