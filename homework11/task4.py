# Завдання 4. 
# Створіть список з назвами улюблених фільмів. 
# Використовуйте метод append() для додавання 
# нових фільмів до списку, метод remove() для 
# видалення фільму, який ви більше не вважаєте 
# улюбленим, і метод sort() для впорядкування 
# списку за алфавітом.


favorite_movies = ["Inception", "The Matrix", "Interstellar"]

# Додати новий фільм
favorite_movies.append("Fight Club")

# Видалити фільм
favorite_movies.remove("The Matrix")

# Впорядкувати список за алфавітом
favorite_movies.sort()

print(favorite_movies)
