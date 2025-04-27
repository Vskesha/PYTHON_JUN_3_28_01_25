# Завдання 3
# Створіть словник для збереження адрес друзів. 
# Ключами будуть імена друзів, а значеннями — 
# словники, що містять вулицю, місто та поштовий 
# код. Додайте адреси для трьох друзів та 
# виведіть адресу одного з них.

friends_addresses = {
    "John Doe": {
        "street": "123 Main St",
        "city": "New York",
        "zip_code": "10001"
    },
    "Jane Smith": {
        "street": "456 Elm St",
        "city": "Los Angeles",
        "zip_code": "90001"
    },
    "Alice Johnson": {
        "street": "789 Oak St",
        "city": "Chicago",
        "zip_code": "60601"
    }
}

print(friends_addresses["John Doe"]["street"])
