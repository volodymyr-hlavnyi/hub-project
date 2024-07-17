from dateutil.relativedelta import relativedelta
from datetime import datetime


# 1.Написать функцию validateCustomers(customer),
# которая принимает на входе список кортежей:
# ●Имя
# ●Фамилия
# ●Дата рождения
# ●Номер банковского счета (iban)
#
# Функция возвращает мапу,
# где ключом является строка имя+фамилия,
# а значением - список сообщений об ошибках,
# возникших при валидации пользователя по следующим правилам:
# ●Имя и фамилия не должны быть пустыми.
# ●Возраст валиден, если он больше 18 лет.
# ●Iban должен соответствовать стандарту длины (начинаться с кода страны и содержать правильное количество символов)
# Решение должно использовать исключения и итераторы.

class ValidateException(Exception):
    pass


class NoNameException(ValidateException):
    pass


class InvalidIbanException(ValidateException):
    pass


class UnallowedAgeException(ValidateException):
    pass


def is_valid_age(date_of_birth_str):
    day, month, year = map(int, date_of_birth_str.split('.'))
    now = datetime.now()
    date_of_birth = datetime(year, month, day)
    difference = relativedelta(now, date_of_birth)
    return difference.years < 18


def is_valid_iban(iban):
    return len(iban) > 15 and len(iban) < 35 and iban.isalnum()


def validate_customers(customers):
    error_map = {}
    for first_name, last_name, birthdate, iban in customers:
        error = []
        try:
            if not first_name:
                raise NoNameException("First name must be filled")
            if not last_name:
                raise NoNameException("Last name must be filled")
            if not is_valid_iban(iban):
                raise InvalidIbanException("Incorrect IBAN")
            if is_valid_age(birthdate):
                raise UnallowedAgeException("Age must be more then 18")
        except NoNameException as e:
            error.append(e)
        except InvalidIbanException as e:
            error.append(e)
        except UnallowedAgeException as e:
            error.append(e)
        error_map.update({f'{first_name} {last_name}': error})

    return error_map


customer_list = [
    ('Viktor', 'Ivanov', '12.12.1996', 'df4345'),
    ('Maria', 'Sidorova', '12.12.2014', 'df435435435345345'),
    ('', 'Sidorova', '12.12.2014', 'df435435435345345'),
]

print(validate_customers(customer_list))
