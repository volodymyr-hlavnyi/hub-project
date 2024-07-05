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