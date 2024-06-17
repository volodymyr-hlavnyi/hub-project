# 1. Напишите программу, которая генерирует
# случайное число от 1 до 100,
# а затем предлагает пользователю угадать это число.
# Если пользователь угадывает число,
# программа выводит сообщение о победе.
# Если пользователь не угадывает число, программа сообщает,
# больше или меньше загаданное число и
# предлагает попробовать снова.
# Используйте цикл с инструкцией break,
# чтобы остановить выполнение цикла, когда число угадано.
#
#
# Пример вывода:
# #
# Угадайте число от 1 до 100: 50
# Загаданное число меньше.
# Попробуйте снова: 75
# Загаданное число больше.
# Попробуйте снова: 63
# Поздравляю! Вы угадали число 63!

import random


def guess_number(user_number, number):
    if user_number == number:
        return f'Congratulation! You guessed the number {number}.'
    elif user_number < number:
        return 'The number is greater.'
    else:
        return 'The number is less.'


def hw_61():
    number = random.randint(1, 100)
    while True:
        user_number = int(input('Guess the number from 1 to 100:'))
        result = guess_number(user_number, number)
        print(result)
        if result.startswith('Congratulation'):
            break


# 2. Напишите программу, которая запрашивает у пользователя число
# N и выводит первые N чисел Фибоначчи.
# Числа Фибоначчи - это последовательность чисел,
# где каждое следующее число является суммой двух предыдущих
# чисел (начиная с 0 и 1).
# Используйте цикл while для решения задачи.
# Выведите числа через запятую с помощью команды print.
#
#
# Пример вывода:
#
# Введите число N: 7
#
# Первые 7 чисел Фибоначчи: 0, 1, 1, 2, 3, 5, 8

def hw_62(num):
    a, b = 0, 1
    i = 0
    numbers_in_line = ''
    while i < num:
        numbers_in_line += f'{a}{"" if i + 1 == num else ", "}'
        a, b = b, a + b
        i += 1
    return (f'First {num} Fibonacci numbers: {numbers_in_line}')


# 3. Напишите программу, которая запрашивает у пользователя целое
# положительное число и проверяет, является ли оно простым.
# Простое число - это число, которое делится только на 1 и
# на само себя без остатка.
# Используйте цикл while и проверку деления числа на все
# числа от 2 до N-1 для решения задачи.
# Выведите соответствующее сообщение на экран с помощью команды print.
#
#
# Пример вывода:
#
# Введите целое положительное число: 17
# Число 17 является простым.

def hw_63(num):
    i = 2
    return_string = ''

    while i < num:
        if num % i == 0:
            return_string = f'Number {num} is not prime.'
            break
        i += 1
    else:
        return_string = f'Number {num} is prime.'

    return return_string


if __name__ == '__main__':
    print('6 1.')
    hw_61()

    print('6 2.')
    num = int(input('Enter a integer for N: '))
    print(hw_62(num))

    print('6 3.')
    num = int(input('Enter a positive integer: '))
    print(hw_63(num))
