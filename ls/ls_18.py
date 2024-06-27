def ls18_1():
    a = [66.25, 333, 333, 1, 1234.5]
    print(a)
    a.insert(2, -1)
    print(a)
    a.remove(333)
    print(a)
    print(f'a.index(-1) {a.index(-1)}')
    print(f'a.count(333) {a.count(333)}')


def ls18_2():
    a = [1, 2, 3, 4, 2]
    a.remove(2)
    print(a)
    a.remove(2)
    print(a)
    print(a.pop(1))
    print(a.pop())
    print(a)


def ls18_3():
    a = [1, 2, 3, 4, 2]
    print(a.count(2))
    a.clear()
    print(a, len(a))
    del a
    a = []
    print(a)


def ls18_4():
    people = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]
    print(people)
    del people[1]
    print(people)
    del people[:3]
    print(people)
    del people[1:]
    print(people)


def ls18_5():
    a = [(18, 'Jane'), (22, 'Tom'), (25, 'Alice'), ('21', 'Sam')]
    for person in a:
        # print(person[0], person[1])
        print(*person[::-1])
        for tp in person:
            print(tp, type(tp))


def ls18_6():
    a = tuple('hello, word!')
    print(a)


def ls18_7():
    a = [1, 2, 3, 4, 5]


# 2.В функцию передаются длинная строка и
# длинный список.
# Надо вставить элементы из списка в строку
# следующим образом: для каждого элемента
# случайно определить позицию для вставки и
# вставить этот элемент по индексу.
# Решите задачу методами для строк и
# методами для списков.
def ls18_8_input():
    string_long = input("Enter the string: ")
    list_long = input("Enter the list: ")
    return string_long, list_long


def ls18_8(string_long, list_long):
    import random
    red_color = "\033[91m"
    reset_color = "\033[0m"
    for symbol in list_long:
        index = random.randint(0, len(string_long))
        string_long = f'{string_long[:index]}{red_color}{str(symbol)}{reset_color}{string_long[index:]}'
    return string_long


if __name__ == '__main__':
    # ls18_1()
    # print('---')
    # ls18_2()
    # print('---')
    # ls18_3()
    # ls18_4()
    # ls18_5()
    # ls18_6()
    str1, list1 = ls18_8_input()
    if len(str1) == 0:
        str1 = 'Hello, world! Supper long string.'
    if len(list1) == 0:
        list1 = ['1', 'rot', 'gelb', '23456']
    print(str1)
    print(list1)
    print(ls18_8(str1, list1))
