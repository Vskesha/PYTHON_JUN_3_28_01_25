movie_list = [
    "Lord of the Rings",
    "The Catcher in the Rye"
    "Game of Thrones",
    "The Shawshank Redemption",
    "Harry Potter",
    "The Da Vinci Code",
]

# Видалити:
# "Game of Thrones" - видалити по індексу
# "The Da Vinci Code" - видалити по значенню

# Додати:
# "The Hobbit",
# "Pride and Prejudice",

movie_list.pop(2)  # Remove "Game of Thrones" by index
movie_list.remove("The Da Vinci Code")  # Remove "The Da Vinci Code" by value

movie_list.append("The Hobbit")  # Add "The Hobbit"
movie_list.append("Pride and Prejudice")  # Add "Pride and Prejudice"

movie_list.sort()

for movie in movie_list:
    print(movie)
