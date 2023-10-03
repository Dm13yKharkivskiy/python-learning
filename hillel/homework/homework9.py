import re


def validation_home_phone_number(phone_number: str) -> bool:
    pattern = r'\d{11}'
    return bool(re.fullmatch(pattern, phone_number))


def validation_mobile_phone_number(phone_number: str) -> bool:
    pattern = r'\+?380*\d{9}'
    return bool(re.fullmatch(pattern, phone_number))


def validation_email(email: str) -> bool:
    pattern = r'\w{3,30}@{1}(gmail.com|mail.ua|ukr.net)'
    return bool(re.fullmatch(pattern, email))


def validation_surname_name_patronymic(name: str) -> bool:
    pattern = r'[A-z]{2,20}\s{1}[A-z]{2,20}\s[A-z]{2,20}'
    return bool(re.fullmatch(pattern, name))


def validation_password(password: str) -> bool:
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,16}$'
    return bool(re.match(pattern, password))

try:
    user_home_phone_number = input("Enter your home phone number(only digits, length - 11): ")
    is_valid_home_phone_number = validation_home_phone_number(user_home_phone_number)
    print(f"Number {user_home_phone_number} is valid: {is_valid_home_phone_number}")

    user_mobile_phone_number = input("Enter your mobile phone number(only digits, length - 12): ")
    is_valid_mobile_phone_number = validation_mobile_phone_number(user_mobile_phone_number)
    print(f"Number {user_mobile_phone_number} is valid: {is_valid_mobile_phone_number}")

    user_email = input("Enter your email(gmail.com, mail.ua, ukr.net): ")
    is_valid_email = validation_email(user_email)
    print(f"Email {user_email} is valid: {is_valid_email}")

    user_name = input("Enter your name(surname, name, patronymic): ")
    is_valid_name = validation_surname_name_patronymic(user_name)
    print(f"Email {user_name} is valid: {is_valid_name}")

    user_password = input("Enter your password(length between 8 and 16, digits, upper and lower symbol): ")
    is_valid_password = validation_password(user_password)
    print(f"Password {user_password} is valid: {is_valid_password}")
except Exception as error:
    print(f"Exception {error}")




