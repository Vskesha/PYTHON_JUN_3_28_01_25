num = float(input("Введіть число: "))

exponent = int(input("Введіть степінь: "))

power_result = num ** exponent
print(f"{num} піднесене до степеня {exponent} дорівнює {power_result}")

absolute_value = abs(num)
print(f"Абсолютне значення числа {num} дорівнює {absolute_value}")

rounded_value = round(num)
print(f"Число {num} округлене до найближчого цілого дорівнює {rounded_value}")

rounded_value_two_decimals = round(num, 2)
print(f"Число {num} округлене до двох десяткових знаків дорівнює {rounded_value_two_decimals}")

input("Для завершення натисніть Enter.")
