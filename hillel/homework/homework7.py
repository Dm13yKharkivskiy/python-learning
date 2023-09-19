import random, math


# Завдання 1

def get_multiplication_nums_list(nums_list: list):
    multiplication_nums = 1
    for num in nums_list:
        multiplication_nums *= num
    return multiplication_nums


length_list = 5
numbers_list = [random.randint(1, 7) for i in range(length_list)]
result_mult_nums = get_multiplication_nums_list(numbers_list)

print(f"List numbers: {numbers_list}")
print(f"Multiplication numbers: {result_mult_nums}")


# Завдання 2


def get_min_max_numbers(nums_list: list):
    min_num = min(nums_list)
    max_num = max(nums_list)
    return min_num, max_num


min_number, max_number = get_min_max_numbers(numbers_list)
print(f"Min number: {min_number}")
print(f"Max number: {max_number}")


# Завдання 3


def get_prime_numbers(nums_list: list):
    count_prime_nums = 0
    count_divisions = 0
    for num in nums_list:
        for i in range(1, num + 1):
            if num % i == 0:
                count_divisions += 1
            if count_divisions > 2:
                break
        if count_divisions == 2:
            count_prime_nums += 1
        count_divisions = 0

    return count_prime_nums


count_prime_numbers = get_prime_numbers(numbers_list)
print(f"Count_prime_numbers: {count_prime_numbers}")


# Завдання 4


def delete_number_from_list(nums_list: list, number):
    count_delete_nums = 0
    while nums_list.count(number):
        nums_list.remove(number)
        count_delete_nums += 1

    return count_delete_nums


number_for_delete = 3
count_delete_numbers = delete_number_from_list(nums_list=numbers_list, number=number_for_delete)
print(f"Count delete number {number_for_delete}: {count_delete_numbers}. List after delete: {numbers_list}")


# Завдання 5


def get_join_two_lists(list_first: list, list_second: list) -> list:
    join_list = list_1 + list_2
    return join_list


list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7]

result_list = get_join_two_lists(list_1, list_2)
print(f"\nList first: {list_1}. List second: {list_2}. Result list: {result_list}")


# Завдання 6

def get_numbers_list_pow(nums_list: list, power_num) -> list:
    power_list = []
    for num in nums_list:
        power_list.append(int(math.pow(num, power_num)))

    return power_list


power_number = 2
result_power_list = get_numbers_list_pow(numbers_list, power_number)
print(f"\nList: {numbers_list}. List number to the power {power_number}: {result_power_list}")
