# обробка винятків

n1, n2 = 10, 0
print(n1 / n2)

num = float(input("Enter the number: "))
print(num)
print(int(num))

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


# генерування власного повідомлення винятка

try:
    name = input("Enter you name: ")

    if 1 < len(name) <= 20:
        print(f"Hello, {name}")
    else:
        raise Exception("Please enter a valid name!")
except Exception as e:
    print(f"Error: {e}")

# match

try:
    print("1. Star game\n2. Settings")
    user_select = int(input("Enter menu number: "))

    # if user_select == 1:
    #     print("Game started")
    # elif user_select == 2:
    #     print("Setting opened")
    # else:
    #     print("Incorrect menu item!")

    match user_select:
        case 1:
            print("Game started")
        case 2:
            print("Incorrect menu item!")
        case _:
            print("Incorrect menu item!")
except Exception as e:
    print(f"Error: {e}")


# цикли

i = 0
while i < 10:
    print(i, end=" ")
    i += 1

sum_numbers = 0
numbers_count = 0

while True:
    user_number = int(input("Enter number: "))

    if user_number == 0:
        print("end...")
        break

    sum_numbers += user_number
    numbers_count += 1

print(f"Sum: {sum_numbers}")
avarage = sum_numbers / numbers_count
print(f"Avg: {sum_numbers}")