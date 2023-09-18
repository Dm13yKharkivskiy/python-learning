# Кортеж (tuple)

# info = ("test", 123)
# print(info)
# print(type(info))
#
#
# info = "test2", 123, 2.3
# print(type(info))

# info = ("test", 123, 2.4)
# info_list = list(info)
# print(info_list)

# for num in 1, 2, 3, 4, 5, 6, "Hello", 7:
#     print(num)

# for _ in range(5):
#     print("Hello")

# print(range(5))

# numbers = list(range(10))
# print(numbers)
#
# numbers_2 = tuple(range(10, 0, -1))
# print(numbers_2)
#
# result = sorted(numbers_2)
# print(result)

# numbers_1 = []
# for i in range(10):
#     numbers_1.append(i)
#
# print(numbers_1)
#
# numbers_2 = [i for i in range(10)]
# print(numbers_2)
#
# numbers_3 = [i for i in range(10) if i > 5]
# print(numbers_3)

# словник (dict)
# users = {
#     1: "John",
#     2: "Vasya",
#     3: "Petya"
# }

# print(type(users))
# print(users[1])
# print(users[3])
# print(users)
# try:
#     print(users[4])
# except KeyError as error:
#     print(f"KeyError: {error}")

# users_list = list(users)
# print(users_list)

# print(users)
# users[1] = "Petya"
# print(users)
# users[4] = "Tom"
# print(users)
#
# for key in users:
#     print(users[key], end=" ")
# print()
# for key in users.keys():
#     print(key, end=" ")
# print()
# print(users.keys())
# print(users.values())
# print(type(users.values()))
#
# print(users.items())
# print(list(users.items()))
#
# for key, value in users.items():
#     print(f"Key: {key} value: {value}")


# users = {
#     1: "John",
#     2: "Vasya",
#     3: "Petya"
# }

# print(users.get(1, "keys not exists"))
#
# # del users[1]
# print(users)
# users.pop(1, "keys not exists")
# print(users)

# users.update(users)
# print(users)

# json

# users = {
#     "Vasya": {
#         "phone": "33333",
#         "email": "sfsfsfsf",
#         "hobbies": ["one", "two", "three"]
#
#     }
# }

# Множини (set)
# users = {"Tom", "Bob", "Tom"}
# print(users)
# users.add("Alice")
# print(users)
#
# users.remove("Tom")
# users.discard("Tom")

# users = {"Tom", "Bob", "Alice"}
# users2 = {"Tom", "Bob", "Alice", "Sam", "Kate"}
# users3 = users.intersection(users2)
# print(users3)
# print(users & users2)

# frozen set не змінна set (множина)
# users = frozenset({"Tom", "Bob"})

import random
import string
password_source_data = string.digits + string.ascii_letters + string.punctuation
