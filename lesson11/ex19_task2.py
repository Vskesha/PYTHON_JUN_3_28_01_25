user_input = input("Введіть число з плаваючою комою: ")

float_value = float(user_input)
rounded_value = round(float_value)

print(f"Округлене ціле число: {rounded_value}")
print(f"Округлене число у вигляді рядка: {str(rounded_value)}")
