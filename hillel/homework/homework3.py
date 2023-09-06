# task 1

try:
    user_select = int(input("Choose a number from 1 to 7: "))

    match user_select:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Incorrect menu item!")
except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception: {error}")

# task 2

try:
    number1, number2 = int(input("Enter first number: ")), int(input("Enter second number: "))

    if number1 == number2:
        print("The numbers are equal")
    else:
        print("Numbers are displayed in ascending order: ")
        if number1 > number2:
            print(number2, number1, sep="\n")
        else:
            print(number1, number2, sep="\n")
except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception: {error}")

# task 3

try:
    number_1, number_2 = int(input("Enter first number: ")), int(input("Enter second number: "))
    select_math_operator = input("Enter operator (+, -, *, /): " )

    match select_math_operator:
        case "+":
            sum_numbers = number_1 + number_2
            print(f"{number_1} {select_math_operator} {number_2} = {sum_numbers}")
        case "-":
            diff_numbers = number_1 - number_2
            print(f"{number_1} {select_math_operator} {number_2} = {diff_numbers}")
        case "*":
            mult_numbers = number_1 * number_2
            print(f"{number_1} {select_math_operator} {number_2} = {mult_numbers}")
        case "/":
            div_numbers = number_1 / number_2
            print(f"{number_1} {select_math_operator} {number_2} = {div_numbers}")
        case _:
                raise Exception("Incorrect select operator!")
except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"Value error: {error}")
except ZeroDivisionError as error:
    print(f"ZeroDivisionError: {error}")
except Exception as error:
    print(f"Error: {error}")