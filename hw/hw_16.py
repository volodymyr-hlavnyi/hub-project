# Python: домашние задание 16 morning(Python)
#
# 1. Напишите программу, которая принимает матрицу (вложенный список) от пользователя и
# находит сумму всех элементов в матрице. Используйте вложенные списки
# и циклы для обхода элементов матрицы.
#
#
# Пример матрицы: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# Пример вывода:
#
# Сумма элементов в матрице: 45
#
def hw16_1_input():
    matrix = []
    while True:
        try:
            row = input('Enter row of matrix (empty string to finish): ')
            if row == '':
                break
            matrix.append([int(x) for x in row.split()])
        except ValueError:
            print('Invalid input. Try again')
    return matrix


def hw16_1(matrix):
    sum_matrix = 0
    for row in matrix:
        for element in row:
            sum_matrix += element
    return sum_matrix


# 2. Напишите программу, которая принимает список чисел от пользователя и
# сортирует его в порядке убывания, используя метод sort() и параметр reverse=True.
# Выведите отсортированный список на экран.
#
#
# Пример вывода:
#
#
# Введите список чисел, разделенных пробелами: 5 2 8 1 3
#
# Отсортированный список чисел: [8, 5, 3, 2, 1]

def hw16_2_input():
    return [int(x) for x in input('Enter list of numbers separated by space: ').split()]


def hw16_2(numbers):
    numbers.sort(reverse=True)
    return numbers


if __name__ == '__main__':
    print('Task 1')
    matrix = hw16_1_input()
    print(f'Sum of elements in matrix: {hw16_1(matrix)}')

    print('Task 2')
    numbers = hw16_2_input()
    print(f'Sorted list of numbers: {hw16_2(numbers)}')