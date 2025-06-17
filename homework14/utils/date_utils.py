"""
Створіть модуль date_utils.py, який міститиме функції для роботи з 
датами. Функції повинні виконувати наступні операції:
Перевіряти, чи є рік високосним (is_leap_year).
Обчислювати кількість днів між двома датами (days_between_dates).
Форматувати дату у вигляді "DD-MM-YYYY" (format_date).
У файлі main.py імпортуйте модуль date_utils та використовуйте функції для роботи з датами.
"""

from datetime import datetime

def is_leap_year(year: int) -> bool:
    """
    Checks if a year is a leap year.
    Перевіряє чи рік високосний.
    
    Args:
        year (int): The year to check. Рік для перевірки.
    Returns:
        bool: True if the year is a leap year, False otherwise. True, якщо рік високосний, False в іншому випадку.
    """
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def days_between_dates(date_str1: str, date_str2: str) -> int:
    """
    Calculates the number of days between two dates.
    Обчислює кількість днів між двома датами.
    
    Args:
        date_str1 (str): The first date in the format "DD.MM.YYYY". Перша дата у вигляді "DD.MM.YYYY".
        date_str2 (str): The second date in the format "DD.MM.YYYY". Друга дата у вигляді "DD.MM.YYYY".
    Returns:
        int: The number of days between the two dates.
    """
    date1 = datetime.strptime(date_str1, "%d.%m.%Y")
    date2 = datetime.strptime(date_str2, "%d.%m.%Y")
    delta = date2 - date1
    return delta.days


def format_date(date_str: str) -> str:
    """
    Formats a date to the format "DD-MM-YYYY".
    Форматує дату у вигляді "DD-MM-YYYY".

    Args:
        date_str (str): The date in the format "DD.MM.YYYY". Дата у вигляді "DD.MM.YYYY" для форматування.
    Returns:
        str: The formatted date in the format "DD-MM-YYYY". Форматована дата у вигляді "DD-MM-YYYY".
    """
    date = datetime.strptime(date_str, "%d.%m.%Y")
    new_date_str = date.strftime("%d-%m-%Y")
    return new_date_str
