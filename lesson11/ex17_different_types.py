user_input = input("Введіть число: ")

int_value = int(user_input)
print(f"Ціле число: {int_value}")

float_value = float(user_input)
print(f"Число з плаваючою комою: {float_value}")

str_int_value = str(int_value)
print(f"Рядок з цілого числа: {str_int_value}")

str_float_value = str(float_value)
print(f"Рядок з числа з плаваючою комою: {str_float_value}")

input("Для завершення натисніть Enter.")
