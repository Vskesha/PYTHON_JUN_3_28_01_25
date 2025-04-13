# str.strip(chars)

text = "   Hello, World!   "
print(text)

cleaned_text = text.strip()
print(cleaned_text)

text2 = "---Hello, world!---"
print(text2)

cleaned_text2 = text2.strip("eH-")
print(cleaned_text2)
