fruits = {"apple", "banana", "cherry"}

# Додавання нового елемента
fruits.add("orange")
print("Після додавання апельсину:", fruits)

# Видалення елемента
fruits.remove("banana")
print("Після видалення банану:", fruits)

# Видалення елемента, якого немає у множині
fruits.remove("kiwi")  # discard
print("Після видалення ківі:", fruits)
