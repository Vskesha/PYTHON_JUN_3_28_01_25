"""
Завдання 3.
Напишіть програму, яка створює таблицю множення
від 1 до 20. Використовуйте вкладені цикли для
створення рядків і стовпців таблиці.
"""

max_num = 20
for i in range(1, max_num + 1):
    for j in range(1, max_num + 1):
        print(f"{i * j:>5}", end="")
    print()

# max_num = 20
# 
# indent = len(str(max_num ** 2)) + 2
# 
# print(" " * indent, "|", end="")
# 
# for i in range(1, max_num + 1):
    # print(f"{i:>{indent}}", end="")
# 
# print()
# print("-" * (indent * (max_num + 1) + 2))
# 
# for i in range(1, max_num + 1):
    # print(f"{i:>{indent}}", "|", end="")
    # for j in range(1, max_num + 1):
        # print(f"{i * j:>{indent}}", end="")
    # print()
