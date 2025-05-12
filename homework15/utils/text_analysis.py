"""
Створіть модуль text_analysis.py, який міститиме функції для аналізу 
тексту. Функції повинні виконувати наступні операції:
Підрахунок кількості речень у тексті (count_sentences).
Знаходити найбільш часто вживане слово (most_frequent_word).
Знаходити найдовше слово в тексті (longest_word).
У файлі main.py імпортуйте модуль text_analysis та використовуйте функції для аналізу тексту.
"""

import re


def count_sentences(text: str) -> int:
    """
    Calculate the number of sentences in the given text. Визначає кількість речень у тексті.

    Args:
        text (str): The given text. Текст у якому буде визначено кількість речень.
    Returns:
        int: The number of sentences in the given text. Кількість речень у вказаному тексті.
    """
    counter = 0
    i = 0
    while i < len(text):
        if text[i] in ".!?":
            counter += 1
            while i < len(text) and not text[i].isalpha():
                i += 1
        i += 1
    
    return counter


def get_words(text: str) -> list[str]:
    """
    Extract words from the given text. Отримує слова з тексту.

    Args:
        text (str): The given text. Текст у якому будуть визначені слова.
    Returns:
        list: A list of words extracted from the given text. Список слів з тексту у нижньому регістрі.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return words


def most_frequent_word(text: str) -> str:
    """
    Find the most frequent word in the given text. Знаходить найбільш часто вживане слово у тексті.

    Args:
        text (str): The given text. Текст для аналізу.
    Returns:
        str: The most frequent word in the given text. Найбільш часто вживане слово у вказаному тексті.
    """
    words = get_words(text)
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


def longest_word(text: str) -> str:
    """
    Find the longest word in the given text. Знаходить найдовше слово у тексті.

    Args:
        text (str): The given text. Текст для аналізу.
    Returns:
        str: The longest word in the given text. Найдовше слово у вказаному тексті.
    """
    words = get_words(text)
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word
