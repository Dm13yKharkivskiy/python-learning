# Початок домашньої роботи, commit до гілки master (перший комміт)

# Перше завдання домашньої роботи №2

number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
number3 = int(input("Введіть третє число: "))
choice = int(input("Що бажаєте зробити з числами?:\n1 - максимальне число\n2 - мінімальне число\n3 - "
                   "середньоарифметичне\n"))

max_number = number1
min_number = number1

if 1 <= choice <= 3:
    if choice == 1:
        if number1 == number2 == number3:
            print("Числа однакові")
        else:
            if number2 > max_number:
                max_number = number2
            if number3 > max_number:
                max_number = number3
            print(f"Максимальне число - {max_number}")
    elif choice == 2:
        if number1 == number2 == number3:
            print("Числа однакові")
        else:
            if number2 < min_number:
                min_number = number2
            if number3 < min_number:
                min_number = number3
            print(f"Мінімальне число - {min_number}")
    elif choice == 3:
        avg_numbers = (number1 + number2 + number3) / 3
        print(f"Cередньоарифметичне - {avg_numbers}")
else:
    print("Неправильний вибір!")


# Друге завдання домашньої роботи №2

count_meters = float(input("Введіть кількість метрів: "))
choice_meters = int(input("В яку одиницю виміру бажаєте перевести метри?:\n1 - милі\n2 - дюйми\n3 - "
                   "ярди\n"))

if choice_meters == 1:
    miles = count_meters * 0.000621371
    print(f"{count_meters} метрів - це {miles} милі")
elif choice_meters == 2:
    inches = count_meters * 39.3701
    print(f"{count_meters} метрів - це {inches} дюйми")
elif choice_meters == 3:
    yards = count_meters * 1.09361
    print(f"{count_meters} метрів - це {yards} ярди")
else:
    print("Неправильний вибір!")