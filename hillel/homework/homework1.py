# Завдання №1
print("Необхідно ввести 3 числа")
number1 = int(input("Введіть 1 число: "))
number2 = int(input("Введіть 2 число: "))
number3 = int(input("Введіть 2 число: "))
addition = number1 + number2 + number3
multiplication = number1 * number2 * number3
print("Сума чисел: ", addition)
print("Добуток чисел: ", multiplication, "\n")

# Завдання №2
print("Для обчислення площі ромба необхідно ввести довжини 2 діагоналей")
d1 = int(input("1 діагональ: "))
d2 = int(input("2 діагональ: "))
square = (d1 * d2) / 2
print("Площа ромба: " + str(square), "\n")

# Завдання №3
number4 = int(input("Введіть чотиризначне число: "))
digit1 = number4 // 1000
digit2 = (number4 // 100) % 10
digit3 = (number4 // 10) % 10
digit4 = number4 % 10
addition_digits = digit1 * digit2 * digit3 * digit4
print(f"Добуток цифр числа: {digit1} * {digit2} * {digit3} * {digit4} = {addition_digits}")