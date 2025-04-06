num1 = input("Введіть перше число:  ")
num2 = input("Введіть друге число:  ")

int_num1 = int(num1)
int_num2 = int(num2)
sum_int = int_num1 + int_num2

print(f"Сума у вигляді цілого числа: {sum_int}")
print(f"Сума у вигляді дійсного числа: {float(sum_int)}")
print(f"Сума у вигляді рядка: {str(sum_int)}")
