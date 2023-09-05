# обробка винятків

# n1, n2 = 10, 0
# print(n1 / n2)

# num = float(input("Enter the number: "))
# print(num)
# print(int(num))

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print(f"Result: {result}")
except ZeroDivisionError as error:
    print(f"ZeroDivisionError occurred: {error}")
except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("End of calculation")