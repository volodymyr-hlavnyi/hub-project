# 1. Напишите программу, которая принимает
# два числа и возвращает их сумму и произведение в виде кортежа
# (sum, product).
# Используйте функцию для вычисления суммы и произведения.
# Выведите результат на экран с помощью команды print.
#
#
# Пример вывода:
#
# Введите первое число: 3
#
# Введите второе число: 4
#
# Сумма и произведение чисел: (7, 12)
def hw13_1_input():
    num1, num2 = map(int, input("Enter num1 and num2: ").split())
    return num1, num2


def hw13_1(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product


# 2. Напишите программу, которая принимает список чисел и
# возвращает сумму, минимальное и максимальное значение из списка.
# Используйте функцию для обработки списка чисел и
# возврата трех значений.
# Выведите результат на экран с помощью команды print.
#
#
# Пример вывода:
#
# Введите числа:  3, 7, 2, 9, 1, 5
#
# Сумма чисел: 27
# Минимальное значение: 1
# Максимальное значение: 9
def hw13_2_input():
    list_numbers_string = list(input("Enter numbers: ").split(','))
    return list(map(int, list_numbers_string))


def hw13_2(list_numbers):
    return sum(list_numbers), min(list_numbers), max(list_numbers)


if __name__ == '__main__':
    num1, num2 = hw13_1_input()
    print(f'Result sum and product: {hw13_1(num1, num2)}')

    list_numbers = hw13_2_input()
    sum_numbers, min_numbers, max_numbers = hw13_2(list_numbers)
    print(f'Sum numbers: {sum_numbers}')
    print(f'Min number: {min_numbers}')
    print(f'Max number: {max_numbers}')
