import text_utils
from utils import string_operations as so

sample_text = "hello world this is a test"

word_count = text_utils.count_words(sample_text)
reversed_text = text_utils.reverse_text(sample_text)
capitalized_text = text_utils.capitalize_text(sample_text)
uppercase_text = so.to_uppercase(sample_text)
lowercase_text = so.to_lowercase(sample_text)

print(f"Word count: {word_count}")
print(f"Reversed text: {reversed_text}")
print(f"Capitalized text: {capitalized_text}")
print(f"Uppercase text: {uppercase_text}")
print(f"Lowercase text: {lowercase_text}")
