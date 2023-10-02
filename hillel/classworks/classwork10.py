from decimal import *

# number = 0.1 + 0.1 + 0.1
#
# print(number)
#
# number = Decimal("0.1")
# number = number + number + number
# print(number)
#
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.00"))
# print(number)

import datetime as dt

# print(dt.date.today())
# print(dt.datetime.now())
# print(dt.datetime.now().second)
#
# my_date = dt.datetime.strptime("12.03.2020", "%d.%m.%Y")
# print(my_date)


from datetime import datetime, timezone, timedelta

# naive = datetime.now()
# print("Naive DateTime:", naive)
#
# UTC = datetime.now(timezone.utc)
# print("UTC DateTime", UTC)
#
# jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'JST'))
# print("In JST::", jst_dateTime)

# numbers = [i for i in range(5) if i % 2 != 0]
# print(numbers)


# generator = (i for i in range(3))
#
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)

# def create_generator():
#     number = 1
#     while True:
#         yield number
#         number += 1
#
#
# my_gen = create_generator()
# print(my_gen)
#
# for i in my_gen:
#     print(i)
#     if i > 10:
#         my_gen.close()


# def demo_gen():
#     yield 1
#     yield 2
#
#
# for i in demo_gen():
#     print(i)

import re


# result = re.match(f'he', 'hello word hello')
# print(result)
#
# result = re.search(f'word', 'hello word hello')
# print(result.start())
# print(result.end())
#
# result = re.findall(f'he', 'hello word hello')
# print(result)
#
# pattern = re.compile('hello')
# result = pattern.findall('hello word hello')

result = re.findall(r'.', "It is a long string")
print(result)

result = re.findall(r'\w*', "It is a long string")
print(result)

result = re.findall(r'\w+', "It is a long string")
print(result)

