import time


# Написать программу, вычисляющую факториал числа.
# Решить задачу с помощью рекурсии.

def hw18_1_input():
    n = int(input('Enter a number: '))
    return n


def hw18_1(n):
    if n == 0:
        return 1
    return n * hw18_1(n - 1)


def hw18_1_output(factorial):
    print(f'Facorial = {factorial}')


# Напишите программу, которая использует рекурсию для
# вычисления суммы цифр числа. Создайте функцию sum_digits,
# которая принимает один аргумент - число,
# для которого нужно вычислить сумму цифр.
# Используйте условие выхода из рекурсии,
# когда число состоит из одной цифры.
# Выведите результат на экран.
#
#
# Пример вывода:
#
#
# Введите число: 12345
#
# Сумма цифр числа 12345 равна 15

def hw18_2_input_and_convert():
    num_str = input('Enter a number: ')
    lst_str = list(num_str)
    return [int(x) for x in lst_str]


def hw18_2_non_tail(lst):
    if not lst:
        return 0
    return lst[0] + hw18_2_non_tail(lst[1:])


def hw18_2_tail(lst, acc=0):
    if not lst:
        return acc
    return hw18_2_tail(lst[1:], acc + lst[0])


def sum_digits(lst, acc=0):
    if len(lst) == 1:
        acc += lst[0]
        return acc
    return sum_digits(lst[1:], acc + lst[0])


if __name__ == '__main__':
    # 1
    n = hw18_1_input()
    factorial = hw18_1(n)
    hw18_1_output(factorial)

    # 2
    lst = hw18_2_input_and_convert()
    print(sum_digits(lst=lst))

    # print(hw18_2_non_tail(lst=lst))
    # print(hw18_2_tail(lst=lst))
