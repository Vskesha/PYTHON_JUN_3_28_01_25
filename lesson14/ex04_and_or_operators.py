age = input("Введіть свій вік: ")
age = int(age)

if age >= 18 and age <= 65:
    print("Ви в діапазоні працездатного віку.")
else:
    print("Ви не повинні працювати.")


if age < 18 or age > 65:
    print("Ви не повинні працювати.")
else:
    print("Ви в діапазоні працездатного віку.")
