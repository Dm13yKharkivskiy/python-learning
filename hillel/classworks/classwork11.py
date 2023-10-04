
# my_file = open("test.txt", "a")
#
# my_file.write("\ntesting")
# my_file.close()


# with open("test.txt", "a") as test_file:
#     test_file.write("22222")

# with open("test.txt", "r") as test_file:
    # result = test_file.read()
    # print(result)

    # result1 = test_file.readline()
    # print(result1)

    # result2 = test_file.readlines()
    # print(result2)

    # for line in test_file:
    #     print(line, end="")

    # line = test_file.readline()
    # while line:
    #     print(line, end="")
    #     line = test_file.readline()


# import pickle
# FILENAME = "notes.dat"
#
# users = [
#     ["John", "123455"],
#     ["Peter", "566444"],
#     ["Vasya", "1343434"]
# ]
#
# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)
#
# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)
#     print(users_from_file)
#     for user in users_from_file:
#         print(f"Name {user[0]} Phone: {user[1]}")

# import shelve
# FILENAME = "notes"
# with shelve.open(FILENAME) as users:
#     users["John"] = "1234556"


# import csv
#
# FILENAME = "users.csv"
#
# users = [
#     ["John", "123455"],
#     ["Peter", "566444"],
#     ["Vasya", "1343434"]
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
#
# with open(FILENAME, "a", newline="") as file:
#     user = ["Anton", "445464646"]
#     writer = csv.writer(file)
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     writer = csv.reader(file)
#     for line in writer:
#         print(f" {line[0]} {line[1]}")

import os