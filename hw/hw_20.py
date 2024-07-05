# 1. Напишите функцию merge_dicts,
# которая принимает произвольное количество
# словарей в качестве аргументов
# и возвращает новый словарь,
# объединяющий все входные словари.
# Если ключи повторяются, значения должны
# быть объединены в список.
# Функция должна использовать аргумент
# **kwargs для принятия произвольного
# числа аргументов словаря.
#
#
# Пример ввода:
# {'a': 1, 'b': 2}
# {'b': 3, 'c': 4}
# {'c': 5, 'd': 6}
#
# Пример вывода:
#
# {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}

def merge_digit_input():
    list_dicts = []
    dict_input = {}
    while True:
        print(f'Line {len(dict_input) + 1}')
        key = input(f'Enter key (empty string - exit): ')
        if len(key) == 0:
            break
        value = int(input('Enter value: '))
        dict_input[key] = value

        if input("Do you want to enter new line or new value? (l/v): ").lower() != 'l':
            pass
        else:
            list_dicts.append(dict_input)
            dict_input = {}
            continue

    return list_dicts


def merge_digits(*args):
    result = {}
    for arg in args:
        for key, value in arg.items():
            if key in result:
                result[key].append(value)
            else:
                result[key] = [value]
    return result


# 2. Напишите программу, которая принимает
# строку от пользователя и подсчитывает количество
# уникальных символов в этой строке.
# Создайте функцию count_unique_chars, которая
# принимает строку и возвращает количество уникальных
# символов. Выведите результат на экран.
# #
# Пример вывода:
# #
# Введите строку: hello
# # Количество уникальных символов: 4

def count_unique_chars(string_for_check):
    return len(set(string_for_check))


# 3. Напишите программу, которая создает словарь, содержащий информацию
# о студентах и их оценках. Ключами словаря являются имена студентов,
# а значениями - списки оценок. Создайте функцию calculate_average_grade,
# которая принимает словарь с оценками студентов и
# вычисляет средний балл для каждого студента.
# Функция должна возвращать новый словарь, в котором ключами являются
# имена студентов, а значениями - их средний балл.
# Выведите результат на экран.
#
#
# Пример словаря с оценками
#
# grades = {
#     'Alice': [85, 90, 92],
#     'Bob': [78, 80, 84],
#     'Carol': [92, 88, 95]
# }
#
# Пример вывода:
#
# {'Alice': 89.0, 'Bob': 80.66666666666667, 'Carol': 91.66666666666667}

def input_grades():
    grades = {}
    while True:
        student_name = input('Enter student name (empty string - exit): ')
        if len(student_name) == 0:
            break
        grades[student_name] = []
        while True:
            grade = input('Enter grade (empty string - exit): ')
            if len(grade) == 0:
                break
            grades[student_name].append(int(grade))
    return grades


def calculate_average_grade(grades):
    result = {}
    for student, grades_list in grades.items():
        result[student] = sum(grades_list) / len(grades_list)
    return result


if __name__ == '__main__':
    print('1. Merge dicts')
    list_dicts = merge_digit_input()
    if len(list_dicts) == 0:
        list_dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
    print(list_dicts)
    print(merge_digits(*list_dicts))

    print('2. Count unique chars')
    input_string = input('Enter string: ')
    print(f'Count of unique chars: {count_unique_chars(input_string)}')

    print('3. Calculate average grade')
    grades = input_grades()
    if len(grades) == 0:
        grades = {
            'Alice': [85, 90, 92],
            'Bob': [78, 80, 84],
            'Carol': [92, 88, 95]
        }
    print(grades)
    print(calculate_average_grade(grades))

