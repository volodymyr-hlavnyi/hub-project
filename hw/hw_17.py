# Python: домашние задание 17 morning(Python)
#
# 1. Напишите программу, которая принимает список чисел от пользователя
# и передает его в функцию modify_list, которая изменяет элементы списка.
# Функция должна умножить нечетные числа на 2, а четные числа разделить на 2.
# Выведите измененный список на экран. Объясните, почему изменения происходят
# только внутри функции и как работают изменяемые и неизменяемые параметры.
#
# Пример вывода:
#
# Введите список чисел, разделенных пробелами: 1 2 3 4 5
#
# Измененный список чисел: [2, 1, 6, 2, 10]
#
def hw17_1_input():
    return [int(x) for x in input('Enter list of numbers separated by space: ').split()]


def hw17_1(numbers):
    def modify_list(numbers):
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0:
                numbers[i] //= 2
            else:
                numbers[i] *= 2
        return numbers

    return modify_list(numbers)


# 2. Напишите программу, которая принимает произвольное количество аргументов
# от пользователя и передает их в функцию calculate_sum,
# которая возвращает сумму всех аргументов. Используйте оператор *
# при передаче аргументов в функцию. Выведите результат на экран.
#
#
# Пример вывода:
#
#
# Введите числа, разделенные пробелами: 1 2 3 4 5
#
# Сумма чисел: 15

def hw17_2_input():
    return [int(x) for x in input('Enter list of numbers separated by space: ').split()]


def hw17_2(*args):
    return sum(args)


if __name__ == '__main__':
    print('Task 1')
    numbers = hw17_1_input()
    print(f'Modified list of numbers: {hw17_1(numbers)}')

    print('Task 2')
    numbers = hw17_2_input()
    print(f'Sum of numbers: {hw17_2(*numbers)}')
