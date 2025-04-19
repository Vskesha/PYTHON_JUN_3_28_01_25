# Завдання 7. 
# Створіть програму, яка перевіряє, 
# чи є введене слово паліндромом.
# 
# 💡 Паліндром — це слово або фраза, 
# яка читається однаково в обох напрямках, 
# ігноруючи пробіли, пунктуацію та регістр символів.

word1 = "Madam"
word2 = "Next"
word3 = "Hello olleH"

def is_palindrome(word):
    characters = []
    for ch in word.lower():
        if ch != ch.upper():
            characters.append(ch)
            
    new_word = "".join(characters)
    return new_word == new_word[::-1]

print(is_palindrome(word1))  # True
print(is_palindrome(word2))  # False
print(is_palindrome(word3))  # True
