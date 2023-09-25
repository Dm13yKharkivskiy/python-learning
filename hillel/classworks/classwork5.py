# Списки

# numbers_1 = []
# numbers_2 = list()
numbers_3 = [1, 3, 25, 7, 2, 7]

# print(type(numbers_1))

# print(*numbers_3)
print(numbers_3)
#
numbers_3[1] = 1111
print(numbers_3)
print(numbers_3[-1])
#
# for i in range(len(numbers_3)):
#     print(numbers_3[i], end=" ")
#
# print()
#
# for number in numbers_3:
#     print(number, end=" ")

# values = ["one", 12, 12.4, True]
# print(values)

# nums = [1, 3] * 3
# print(nums)

# numbers_3 = [1, 3, 25, 7, 2, 7]
# print(numbers_3[:])
# print(numbers_3[1:5])
# print(numbers_3[::-1])

# users = ["Vasya", "Petya"]
# users_1, users_2 = users
# print(users_1)
# print(users_2)
# print(users)

import random

# # print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
#
# print(numbers)
#
# # numbers.insert(1, 3333)
# # print(numbers)
# #
# # numbers.extend([1, 2, 3])
# # print(numbers)
# #
# # numbers += [2, 2, 2]
# # print(numbers)
# #
# # numbers.remove(3333)
# # print(numbers)
# #
# # # numbers.clear()
# # # print(numbers)
# #
# # del numbers
# # print(numbers)
#
# print(numbers.index(2))
#
# print(numbers.pop(2))
# print(numbers)
# print(numbers.count(3))

# numbers_1 = [5, 2, 4, 1, 5, 3]
# print(numbers_1)
# numbers_1.sort()
# print(numbers_1)
#
# numbers_sorted = sorted(numbers_1)
# print(numbers_sorted)

# people = ["Tom", "Bob", "Alice", "sam", "bill"]
# people.sort(key=str.lower)
# print(people)

# numbers_1 = [5, 2, 4, 1, 5, 3]
# numbers_1.reverse()
# print(numbers_1)

# a = 3
# b = a
# print("a", a)
# print("b", b)
# a = 5
# print("a", a)
# print("b", b)


# text = "hello world. goodbye world."
# search_item = ". "
# sentences = text.split(search_item)
# print(sentences)
# result = []
# for sentence in sentences:
#     result.append(sentence.capitalize())
# print(result)
#
# result_2 = search_item.join(result)
# print(result_2)

# матриці

# matrix = [
#     [1, 2, 3],
#     [3, 2, 1],
#     [4, 4, 5]
# ]
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

# import random
#
# matrix = []
# print(matrix)
#
# for i in range(10):
#     matrix.append([])
#     for j in range(10):
#         matrix[i].append(random.randint(1, 10))
#
# print(matrix)

print(0 % 3)