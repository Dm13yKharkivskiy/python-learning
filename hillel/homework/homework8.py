import math, random

# Завдання 1


def get_pow(number, degree):
    if degree <= 1:
        return number
    else:
        return number * get_pow(number, degree - 1)


try:
    number_enter = int(input("Enter number: "))
    degree_enter = int(input("Enter pow: "))
    degree_number = get_pow(number_enter, degree_enter)

    print(f"Degree number {number_enter} is {degree_number}")
except Exception as error:
    print(error)

# get_pow(2, 3) -> 2 * get_pow(2, 2) => 8
# get_pow(2, 2) -> 2 * get_pow(2, 1) => 4
# 2 * get_pow(2, 1) => 2


# Завдання 2

def print_stars(count_stars):
    if count_stars < 1:
        print("", end="")
    else:
        print_stars(count_stars - 1)
        print("*", end="")


try:
    count_stars_enter = int(input("Enter count stars: "))
    print_stars(count_stars_enter)
    print()
except Exception as error:
    print(error)

# print_stars(3) -> print_stars(2) => ***
# print_stars(2) -> print_stars(1) => **
# print_stars(1) => *
# print_stars(0) => вивід в консоль ""


# Завдання 3


def get_sum(num_a, num_b):
    if num_a >= num_b:
        return num_a
    return num_a + get_sum(num_a + 1, num_b)


try:
    number_a = int(input("Enter number A: "))
    number_b = int(input("Enter number B: "))
    sum_a_b = get_sum(number_a, number_b)
    print(f"Sum numbers {number_a} and {number_b} is {sum_a_b}")
except Exception as error:
    print(f"Error: {error}")

# get_sum(1, 3) -> get_sum(2, 3) => 6
# get_sum(2, 3) -> get_sum(3, 3) => 5
# get_sum(3, 1)  => 3


# Завдання 4


def get_index_min_sum(numbers: list, start_ind, end_ind, min_sum=math.inf, min_ind=0):
    if end_ind < len(numbers):
        current_sum = sum(numbers[start_ind:end_ind + 1])

        if current_sum < min_sum:
            min_sum = current_sum
            min_ind = start_ind

        start_ind += 1
        end_ind += 1

        return get_index_min_sum(numbers, start_ind, end_ind, min_sum, min_ind)
    return min_ind


try:
    nums_list = [random.randint(1, 10) for _ in range(1, 101)]
    print(nums_list)

    start_index = 0
    end_index = 0
    result_min_index = get_index_min_sum(nums_list, start_index, end_index)

    print(f"Start index with min sum: {result_min_index}")
except Exception as error:
    print(error)
