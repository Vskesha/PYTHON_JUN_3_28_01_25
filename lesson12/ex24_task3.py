visitors = ["Ivan", "Oleg", "Andriy", "Yulia", "Sasha"]
new_visitors = ["Maryna", "Natalia", "Volodymyr"]

# Видалити двох учасників зі списку (одного за значенням, а іншого за індексом)
# Додати ще 3 нові імена зі списку new_visitors до списку visitors

visitors.pop(1)
visitors.remove("Sasha")

visitors.extend(new_visitors)
visitors.sort()

print(visitors)
