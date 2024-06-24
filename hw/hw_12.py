# 1. Напишите программу, которая запрашивает у
# пользователя число N и выводит на экран таблицу
# умножения от 1 до N. Используйте вложенный цикл
# for для создания таблицы умножения.
# Выведите результат на экран с помощью команды print.
#
# Пример вывода:
#
# Введите число N: 5
#
# Таблица умножения:
#
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

def hw12_1_input():
    num = int(input("Enter number N: "))
    return num


def hw12_1(num: int = 5, align: str = '>'):
    a = "{:{fill}{align}{width}}"
    max_width = len(str(num * num)) + 1
    for i in range(1, num + 1):
        for k in range(1, num + 1):
            print(a.format(i * k,
                           fill=' ',
                           align=align,
                           width=max_width), end='')

        print()


# 2. Напишите программу, которая принимает два списка
# одинаковой длины и создает новый список, содержащий
# пары элементов из исходных списков.
# Используйте функцию zip() для создания пар элементов.
# Выведите результат на экран с помощью команды print.
#
# Пример вывода:
#
# Введите элементы первого списка, разделенные пробелом: 1 2 3 4 5
# Введите элементы второго списка, разделенные пробелом: A B C D E
#
# Список пар элементов: [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]

def hw12_2_input():
    list1 = input('Enter elements of the first list, separated by space: ')
    list2 = input('Enter elements of the second list, separated by space: ')
    return list1, list2


def hw12_2(list1: str, list2: str):
    list1 = list1.split()
    list2 = list2.split()
    result = list(zip(list1, list2))
    return f'List of pairs of elements: {result}'


if __name__ == '__main__':
    num = hw12_1_input()
    print('When align left (as in homework)')
    hw12_1(num, '<')
    # more beautiful
    # when align align
    print('*' * 50)
    print('When align right')
    hw12_1(num, '>')
    print('*' * 50)

    list1, list2 = hw12_2_input()
    print(hw12_2(list1, list2))
