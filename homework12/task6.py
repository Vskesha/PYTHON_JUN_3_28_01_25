# Завдання 6. 
# Створіть список з декількома елементами, 
# зробіть його копію за допомогою методу copy(), 
# змініть копію, та виведіть обидва списки, 
# щоб показати, що вони різні.


original_list = [1, 2, 3, 4, 5]
copy_list = original_list.copy()

copy_list[0] = 100
copy_list.append(6)

print("Original list:", original_list)
print("Copy list:", copy_list)

# В результаті виводу на екран будуть відображені різні списки.
