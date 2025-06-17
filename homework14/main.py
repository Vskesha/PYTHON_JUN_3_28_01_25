"""
У файлі main.py імпортуйте модуль number_utils та використовуйте функції для перевірки чисел.
У файлі main.py імпортуйте модуль text_analysis та використовуйте функції для аналізу тексту.
У файлі main.py імпортуйте модуль date_utils та використовуйте функції для роботи з датами.
"""

from utils.number_utils import is_prime, factorial, generate_primes
from utils.text_analysis import count_sentences, most_frequent_word, longest_word
from utils.date_utils import is_leap_year, days_between_dates, format_date


# --------------------------------------------------------------------------------------------------------------------
print("Чи є число 17 простим?", is_prime(17))
print("Факторіал числа 5:", factorial(5))
print("Прості числа до 20:", generate_primes(20))
print("-" * 50)


# --------------------------------------------------------------------------------------------------------------------
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel tempor mi. Integer vel ex at felis dictum gravida?! " \
      "Proin non justo vel enim consequat mollis. Sed auctor, nunc vel consectetur fermentum, felis lectus ultrices velit, " \
      "at ultricies felis felis vitae velit. Donec facilisis, lectus vel cursus luctus, ligula est blandit neque, " \
      "euismod enim neque sed nisi... Sed libero est, pellentesque at facilisis at, dignissim non diam. Donec interdum, felis " \
      "vel sagittis tristique, ligula nunc sollicitudin velit, vel pharetra felis felis nec velit!!! Donec vel lectus vel neque " \
      "malesuada facilisis. Sed vel enim vel odio bibendum aliquet."

print("Кількість речень у тексті:", count_sentences(text))
print("Найбільш повторюване слово:", most_frequent_word(text))
print("Найдовше слово:", longest_word(text))
print("-" * 50)

# --------------------------------------------------------------------------------------------------------------------
print("Чи є рік 2024 високосним?", is_leap_year(year=2024))
print("Різниця днів між 19.07.2021 та 25.07.2024:", days_between_dates(date_str1="19.07.2021", date_str2="25.07.2024"))
print("Форматований рік 19.07.2021:", format_date(date_str="19.07.2021"))
print("-" * 50)
