# Функції 2: область видимості змінних, рекурсія, замикання

# def hello(): print("Hello!")
#
#
# print(hello)
# massage = hello
# print(massage)
#
# hello()
# massage()


# message = lambda: print("Hello world!")
#
#
# message()
#
#
# square = lambda side_1, side_2: side_1 * side_2
#
#
# print(square(2, 4))


# def calculate(a, b, math_oper) -> None:
#     print(f"Result: {math_oper(a, b)}")
#
#
# calculate(2, 5, lambda n1, n2: n1 + n2)

number = 10


# def test():
#     global number
#     number = 11
#     print(number)
#
#
# print(number)
# test()
# print(number)


# def outer():
#     number = 1
#
#     def inner():
#         nonlocal number
#         number = 2
#         print(number)
#
#     inner()
#     print(number)
#
#
# outer()

# def show_info(*args):
#     print(args)
#
#
# show_info(1, 3, 2, "asasas")

# def show_user_info(**kwargs):
#     print(kwargs)
#
#
# show_user_info(name="Vasya", age=33)


# def user_info(ids, *args, add_info="demo info", **kwargs):
#     print(ids)
#     print(args)
#     print(add_info)
#     print(kwargs)
#
#
# user_info(3, 1, 2, 3, 4, add_info="student", name="Vasya", age=33)

# def show_info(num1, num2, num3):
#     print(f"{num1} {num2} {num3}")
#
#
# nums = [1, 2, 3]
# show_info(*nums)

# def show_user_info(name, age, hobby):
#     print(f"{name} {age} {hobby}")
#
#
# user_info = {
#     "name": "Vasya",
#     "age": 44,
#     "hobby": "walk"
# }
#
# show_user_info(**user_info)


def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))
