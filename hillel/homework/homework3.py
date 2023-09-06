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
