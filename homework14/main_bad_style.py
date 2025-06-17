"""
У файлі main.py імпортуйте модуль number_utils та використовуйте функції для перевірки чисел.
У файлі main.py імпортуйте модуль text_analysis та використовуйте функції для аналізу тексту.
У файлі main.py імпортуйте модуль date_utils та використовуйте функції для роботи з датами.
"""

import re

def prost(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    if n <= 1:
        return 1
    return n * f(n - 1)

def prost_sp(limit):
    primes = []
    for num in range(2, limit + 1):
        if prost(num):
            primes.append(num)
    return primes

print("Чи є число 17 простим?", prost(17))
print("Факторіал числа 5:", f(5))
print("Прості числа до 20:", prost_sp(20))
print("-" * 50)

def rechennya(text):
    counter = 0
    i = 0
    while i < len(text):
        if text[i] in ".!?":
            counter += 1
            while i < len(text) and not text[i].isalpha():
                i += 1
        i += 1
    
    return counter

def slov(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

def freq(text):
    words = slov(text)
    words_count = {}
    
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    most_frequent_word = ""
    max_count = 0

    for word, count in words_count.items():
        if count > max_count:
            max_count = count
            most_frequent_word = word
    
    return most_frequent_word

def long(text):
    words = slov(text)
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel tempor mi. Integer vel ex at felis dictum gravida?! " \
      "Proin non justo vel enim consequat mollis. Sed auctor, nunc vel consectetur fermentum, felis lectus ultrices velit, " \
      "at ultricies felis felis vitae velit. Donec facilisis, lectus vel cursus luctus, ligula est blandit neque, " \
      "euismod enim neque sed nisi... Sed libero est, pellentesque at facilisis at, dignissim non diam. Donec interdum, felis " \
      "vel sagittis tristique, ligula nunc sollicitudin velit, vel pharetra felis felis nec velit!!! Donec vel lectus vel neque " \
      "malesuada facilisis. Sed vel enim vel odio bibendum aliquet."

print("Кількість речень у тексті:", rechennya(text))
print("Найбільш повторюване слово:", freq(text))
print("Найдовше слово:", long(text))
print("-" * 50)

from datetime import datetime

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def days_between_dates(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, "%d.%m.%Y")
    date2 = datetime.strptime(date_str2, "%d.%m.%Y")
    delta = date2 - date1
    return delta.days

def format_date(date_str):
    date = datetime.strptime(date_str, "%d.%m.%Y")
    new_date_str = date.strftime("%d-%m-%Y")
    return new_date_str

print("Чи є рік 2024 високосним?", is_leap_year(2024))
print("Різниця днів між 19.07.2021 та 25.07.2024:", days_between_dates("19.07.2021", "25.07.2024"))
print("Форматований рік 19.07.2021:", format_date("19.07.2021"))
print("-" * 50)
