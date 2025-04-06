# Цілочисельне ділення
base = 10 // 4
print(base)

# Піднесення до степеня
exponent = 3
result = base ** exponent  # 2 * 2 * 2 = 8
print(f"{base} в степені {exponent} дорівнює {result}!")

# Остача від ділення
number = 15
divisor = 3
remainder = number % divisor  # 10 % 3 | 15 % 3
print(f"Остача від ділення {number} на {divisor} дорівнює {remainder}")

# Абсолютне значення числа
number = -5
absolute_value = abs(number)
print(f"Абсолютне значення числа {number} дорівнює {absolute_value}")

# Округлення числа
number = 5.678
rounded_number = round(number)
print(f"Число {number} округлене до цілого дорівнює {rounded_number}")

rounded_number_two_decimals = round(number, 2)
print(f"Число {number} округлене до двох знаків після коми дорівнює {rounded_number_two_decimals}")
