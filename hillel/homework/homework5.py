import random, copy

# Завдання 1

nums_list = []

for i in range(7):
    nums_list.append(random.randint(-2, 5))

sum_negative_nums = 0
sum_paired_nums = 0
sum_unpaired_nums = 0
mult_nums_index_3 = 1
mult_nums_betw_min_max = 1
sum_nums_betw_positive = 0

min_num = min(nums_list)
max_num = max(nums_list)
index_min = []
index_max = []

index_positive = []

for i in range(len(nums_list)):

    if nums_list[i] < 0:
        sum_negative_nums += nums_list[i]

    if nums_list[i] % 2 == 0 and nums_list[i] != 0:
        sum_paired_nums += nums_list[i]

    if nums_list[i] % 2 != 0 and nums_list[i] != 0:
        sum_unpaired_nums += nums_list[i]

    if i != 0 and i % 3 == 0:
        mult_nums_index_3 *= nums_list[i]

    if nums_list[i] == min_num:
        index_min.append(i)

    if nums_list[i] == max_num:
        index_max.append(i)

    if nums_list[i] > 0:
        index_positive.append(i)

if min(index_min) < max(index_max) and max(index_max) - min(index_min) > 1:
    for i in range(min(index_min) + 1, max(index_max)):
        mult_nums_betw_min_max *= nums_list[i]
elif min(index_max) < max(index_min):
    for i in range(min(index_max) + 1, max(index_min)):
        mult_nums_betw_min_max *= nums_list[i]
else:
    mult_nums_betw_min_max = 0

print(f"List of numbers: {nums_list}")
print(f"Sum negative numbers: {sum_negative_nums}")
print(f"Sum paired numbers: {sum_paired_nums}")
print(f"Sum unpaired numbers: {sum_unpaired_nums}")
print(f"Multiplication numbers with index multiple 3: {mult_nums_index_3}")

print(f"Multiplication numbers between min and max numbers: {mult_nums_betw_min_max}")

if len(index_positive) > 1 and max(index_positive) - min(index_positive) > 1:
    sum_nums_betw_positive = sum(nums_list[min(index_positive) + 1:max(index_positive)])
    print(f"Sum numbers between first and last positive numbers: {sum_nums_betw_positive}")
else:
    print("Sum numbers between first and last positive numbers: no numbers between positive numbers")

# Завдання 2
numbers_2 = []
numbers_paired = []
numbers_unpaired = []
numbers_positive = []
numbers_negative = []

for i in range(5):
    numbers_2.append(random.randint(-5, 5))

for number in numbers_2:
    if number % 2 == 0 and number != 0:
        numbers_paired.append(number)
    if number % 2 != 0:
        numbers_unpaired.append(number)

    if number > 0:
        numbers_positive.append(number)
    if number < 0:
        numbers_negative.append(number)

print(f"\nList of numbers: {numbers_2}")
print(f"List of paired numbers: {numbers_paired}")
print(f"List of unpaired numbers: {numbers_unpaired}")
print(f"List of positive numbers: {numbers_positive}")
print(f"List of negative numbers: {numbers_negative}")

# Додаткове завдання

matrix = []
numbers_main_diagonal = []
numbers_side_diagonal = []
numbers_choice_column = []

for i in range(10):
    matrix.append([])
    for j in range(10):
        matrix[i].append(random.randint(10, 99))

diff_for_side_diagonal = len(matrix) - 1

print("\nMatrix 10x10: ")
for row in range(len(matrix)):
    for i in range(len(matrix[row])):
        print(matrix[row][i], end="\t")
        if row == i:
            numbers_main_diagonal.append(matrix[row][i])
        if i == diff_for_side_diagonal:
            numbers_side_diagonal.append(matrix[row][i])
            diff_for_side_diagonal -= 1

    print()

print(f"\nSum numbers of main diagonal {numbers_main_diagonal}: {sum(numbers_main_diagonal)}")
print(f"Min number of side diagonal {numbers_side_diagonal}: {min(numbers_side_diagonal)}")
print(f"Max number of side diagonal {numbers_side_diagonal}: {max(numbers_side_diagonal)}")

try:
    column_matrix = int(input("\nSelect column matrix (enter number between 1 and 10): "))
    if column_matrix > 10 or column_matrix < 0:
        raise Exception("Please enter number between 1 and 10!")
    else:
        for row in matrix:
            for i in range(len(row)):
                if i == column_matrix - 1:
                    numbers_choice_column.append(row[i])
        print(f"Your choice column matrix {column_matrix}: {numbers_choice_column}")
except ValueError:
    print("Please enter number between 1 and 10!")
except Exception as error:
    print(f"Error: {error}")

try:
    row_matrix = int(input("Select row matrix (enter number between 1 and 10): "))
    if row_matrix > 10 or row_matrix < 1:
        raise Exception("Please enter number between 1 and 10!")
    else:
        print(f"Your choice row matrix {row_matrix}: {matrix[row_matrix - 1]}")
except ValueError:
    print("Please enter number between 1 and 10!")
except Exception as error:
    print(f"Error: {error}")

change_column_matrix = copy.deepcopy(matrix)
change_row_matrix = copy.deepcopy(matrix)

try:
    change_column_first = int(input("\nSelect first column matrix (enter number between 1 and 10): "))
    change_column_second = int(input("Select second column matrix (enter number between 1 and 10): "))

    if change_column_first < 1 or change_column_first > 10 or change_column_second < 1 or change_column_second > 10:
        raise Exception("Incorrect number enter!")
    else:
        for i in range(len(matrix)):
            number_to_first_column = matrix[i][change_column_second - 1]
            number_to_second_column = matrix[i][change_column_first - 1]

            change_column_matrix[i].pop(change_column_first - 1)
            change_column_matrix[i].insert(change_column_first - 1, number_to_first_column)

            change_column_matrix[i].pop(change_column_second - 1)
            change_column_matrix[i].insert(change_column_second - 1, number_to_second_column)

        print(f"\nMatrix with swapped columns {change_column_first} and {change_column_second}: ")

        for i in range(len(change_column_matrix)):
            for j in range(len(change_column_matrix[i])):
                print(change_column_matrix[i][j], end="\t")
            print()

except ValueError:
    print("Incorrect enter!")
except Exception as error:
    print(f"Exception: {error}")

try:
    change_row_first = int(input("\nSelect first row matrix (enter number between 1 and 10): "))
    change_row_second = int(input("Select second row matrix (enter number between 1 and 10): "))

    if change_row_first < 1 or change_row_first > 10 or change_row_second < 1 or change_row_second > 10:
        raise Exception("Incorrect numbers!")
    else:
        change_row_matrix.pop(change_row_first - 1)
        change_row_matrix.insert(change_row_first - 1, matrix[change_row_second - 1])

        change_row_matrix.pop(change_row_second - 1)
        change_row_matrix.insert(change_row_second - 1, matrix[change_row_first - 1])

        print(f"\nMatrix with swapped rows {change_row_first} and {change_row_second}: ")
        for row in change_row_matrix:
            for i in range(len(row)):
                print(row[i], end="\t")
            print()
except ValueError:
    print("Incorrect enter!")
except Exception as error:
    print(f"Exception: {error}")
