# 1. Напишите функцию, которая принимает список кортежей от пользователя,
# где каждый кортеж содержит информацию о студенте (имя, возраст, средний балл).
# Программа должна вывести на экран имена студентов, чей средний балл выше
# заданного значения. Используйте методы кортежей и циклы для обработки данных.
# Выведите итоговый список на экран с помощью команды print.
#
#
# Пример списка кортежей:
#
# [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
#
#
# Пример вывода:
#
# Введите пороговое значение среднего балла: 90
# Студенты с средним баллом выше 90 : ['Charlie']

def hw15_1_input_1():
    students_local = []
    while True:
        name = input('Enter student name: ')
        if len(name) == 0:
            break
        age = int(input('Enter student age: '))
        score = int(input('Enter student score: '))
        students_local.append((name, age, score))
        if input('Do you want to add another student? (y/n): ').lower() != 'y':
            break
    return students_local


def hw15_1_input_2():
    threshold = input('Enter the threshold score: ')
    if len(threshold) == 0:
        threshold = 90
    else:
        threshold = int(threshold)
    return threshold


def hw15_1(students, threshold):
    result = []
    for student in students:
        if student[2] > threshold:
            result.append(student[0])
    return result


# 2. Напишите программу, которая принимает строку от пользователя и
# разбивает ее на отдельные слова. Затем программа должна создать новый кортеж,
# содержащий длину каждого слова в исходной строке. Используйте методы строк и
# кортежей для обработки данных.
#
#
# Пример вывода:
#
# Введите предложение: Программирование это интересно и полезно
# Длины слов в предложении: (15, 3, 8, 2, 6)

def hw15_2_input():
    sentence_local = input('Enter the sentence: ')
    if len(sentence_local) == 0:
        sentence_local = 'Programming is interesting and useful'
    return sentence_local


def hw15_2(sentence_local):
    words = sentence_local.split()
    result_local = tuple(len(word) for word in words)
    return result_local


if __name__ == '__main__':
    students = hw15_1_input_1()
    if len(students) == 0:
        students = [('Alice', 20, 90), ('Bob', 19, 80), ('Charlie', 21, 95), ('David', 18, 85)]
    print(students)
    threshold = hw15_1_input_2()
    result = hw15_1(students, threshold)
    print(f'Students with average score more then {threshold} : {result}')

    sentence = hw15_2_input()
    print(sentence)
    print(hw15_2(sentence_local=sentence))
