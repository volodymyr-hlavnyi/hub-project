# 1. Напишите программу, которая
# запрашивает у пользователя три числа и
# выводит их в порядке возрастания,
# разделенные запятой.
# Используйте условные операторы и
# вложенные условия для решения задачи.
# Предполагается, что все три числа различны.
# Пример вывода:
# Введите первое число: 5
# Введите второе число: 2
# Введите третье число: 7
# Числа в порядке возрастания: 2, 5, 7
def hw5_1_1(num1, num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    return f'Numbers in ascending order: {num1}, {num2}, {num3}'


def hw5_1_2(num1, num2, num3):
    return f'Numbers in ascending order: {", ".join(map(str, sorted([num1, num2, num3])))}'


# 2. Напишите программу, которая запрашивает у
# пользователя год и проверяет,
# является ли он високосным.
# Год является високосным,
# если он делится на 4 без остатка,
# но не делится на 100 без остатка,
# за исключением годов, которые делятся
# на 400 без остатка.
# Выведите соответствующее сообщение
# на экран с помощью команды print.
# Пример вывода:
# Введите год: 2024
# Год является високосным.

def hw5_2(year):
    if (year % 4 == 0
            and year % 100 != 0 or year % 400 == 0):
        return 'The year is a leap year.'
    return 'The year is not a leap year.'


if __name__ == '__main__':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    num3 = int(input('Enter third number: '))

    print(hw5_1_1(num1, num2, num3))

    print(hw5_1_2(num1, num2, num3))

    print(hw5_2(int(input('Enter year: '))))
