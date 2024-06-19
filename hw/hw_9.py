# Python: домашние задание 9 morning(Python)
#
# 1. Напишите программу, которая запрашивает у пользователя
# строку и определяет, является ли она панграммой.
# Панграмма - это фраза, содержащая все буквы алфавита.
# Программа должна игнорировать регистр букв и пробелы при
# проверке панграммы. Выведите соответствующее сообщение на экран
# с помощью команды print. Решить задачу для латиницы.
#
#
# Пример вывода:
##
# Введите строку: The quick brown fox jumps over the lazy dog
##
# Строка является панграммой.
#
def hw9_1(input_string: str = 'The quick brown fox jumps over the lazy dog'):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i not in input_string.lower():
            return "String is not pangram."
    return "String is pangram."


#
# 2. Напишите программу, которая запрашивает у пользователя строку и
# выводит на экран количество гласных и согласных букв в ней.
# Используйте функцию len() для подсчета количества букв.
# Выведите результат на экран с помощью команды print.
# Решить задачу для латиницы.
##
#
# Пример вывода:
#
# Введите строку: Hello World
#
# Количество гласных букв: 3
#
# Количество согласных букв: 7
def hw9_2(input_string: str = 'Hello World'):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    input_string = input_string.lower()
    count_vowels = 0
    count_consonants = 0
    for i in input_string:
        if i in vowels:
            count_vowels += 1
        elif i in consonants:
            count_consonants += 1
    return f"Number of vowels: {count_vowels}\nNumber of consonants: {count_consonants}"


if __name__ == '__main__':
    print(hw9_1())
    print(hw9_2())
