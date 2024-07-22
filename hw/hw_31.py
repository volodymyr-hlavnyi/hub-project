# Python: домашние задание 31 morning (Python)
#
# 1. Напишите декоратор validate_args, который будет проверять типы аргументов функции и выводить сообщение об ошибке, если переданы аргументы неправильного типа. Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.
#
#
# Пример использования:
#
# @validate_args(int, str)
# def greet(age, name):
#     print(f"Привет, {name}! Тебе {age} лет.")
#
#
# greet(25, "Анна")  # Все аргументы имеют правильные типы
#
#
# greet("25", "Анна")  # Возникнет исключение TypeError
#
#
# Ожидаемый вывод:
#
# Привет, Анна! Тебе 25 лет.
# TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.
from functools import wraps


def print_name(func):
    @wraps(func)
    def wrapper():
        print(f'{func.__name__}')
        try:
            func()
        except TypeError as e:
            print(e)
    return wrapper


@print_name
def hw31_1():
    def validate_args(*types):
        def decorator(func):
            def wrapper(*args):
                for arg, arg_type in zip(args, types):
                    if not isinstance(arg, arg_type):
                        raise TypeError(f"Argument {arg} has incorrect type {type(arg)}. Ожидается {arg_type}.")
                return func(*args)

            return wrapper

        return decorator

    @validate_args(int, str)
    def greet(age, name):
        print(f"Hi, {name}! Your are {age} year old.")

    greet(25, "Anna")
    greet("25", "Anna")


# 2. Напишите декоратор log_args,
# который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке
# в формате
# "Аргументы: <аргументы>, Результат: <результат>".
# Используйте модуль logging для записи в лог-файл.
#
# Пример использования:
# python
# @log_args
# def add(a, b):
#     return a + b
#
# add(2, 3)
# add(5, 7)
#
# Ожидаемый вывод в файле log.txt:
# Аргументы: 2, 3, Результат: 5
# Аргументы: 5, 7, Результат: 12
#
# Убедитесь, что перед запуском кода у вас создан файл log.txt
# в той же директории, где находится скрипт Python.
@print_name
def hw31_2():
    import logging

    logging.basicConfig(filename='log.txt', level=logging.INFO)

    def log_args(func):
        def wrapper(*args):
            result = func(*args)
            logging.info(f"Args: {args}, Result: {result}")

        return wrapper

    @log_args
    def add(a, b):
        return a + b

    print("Start writing to log.txt")
    add(2, 3)
    add(5, 7)


if __name__ == '__main__':
    try:
        hw31_1()
    except TypeError as e:
        print(e)

    hw31_2()
