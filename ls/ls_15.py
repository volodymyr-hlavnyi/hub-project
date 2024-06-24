def ls15_1():
    string1 = ''
    for i in range(10):
        string1 += str(i)
    print(', '.join(string1))


def ls15_2():
    string1 = 'fdgkhdfklKJHGUIIUYUfdkgjhfdjkhTYREWGFNMP{'
    for symbol in string1:
        if symbol.isupper():
            string1 = string1.replace(symbol, '')
    print(string1)


def ls15_3():
    print('for i in range(10)')
    for i in range(10):
        print(i, end=' ')

    print('\n\nfor i in range(5, 10)')
    for i in range(5, 10):
        print(i, end=' ')

    print('\n\nfor i in range(0, 10, 2)')
    for i in range(0, 10, 2):
        print(i, end=' ')

    print('\n\nfor i in range(10, 0, -1)')
    for i in range(10, 0, -1):
        print(i, end=' ')

    print('\n\nn = 10 for i in range(2, n+1)')
    n = 10
    for i in range(2, n + 1):
        print(i, end=' ')
    print('\n\nlist(range(2, n + 1))')
    print(list(range(2, n + 1)))


def ls15_4():
    a = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    for index, fruit in enumerate(a):
        print(index, fruit)


def ls15_5():
    a = list(range(10, 1, -3))
    b = []
    for index, num in enumerate(a):
        b.append(f'{index} {num}')
    print(a)
    print(b)


def ls15_6():
    data = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    data_new1 = []
    data_new2 = []
    new_data3 = ()
    for letter, number in data:
        data_new1.append(letter)
        data_new2.append(number)
    new_data3 = (data_new1, data_new2)
    print(type(new_data3))
    print(new_data3)


def ls15_7():
    a = ['Alice', 'Bob', 'Charlie']
    b = [15, 20, 12]
    for name, age in zip(a, b):
        print(name, age)


def ls15_8(name_file, lines):
    with open(name_file, 'r') as file:
        lines_str = file.readlines()
    last_lines1 = lines_str[-lines:]
    # print(last_lines1)
    last_lines2 = ''
    for line in last_lines1:
        last_lines2 += line
    return last_lines2


if __name__ == '__main__':
    ls15_1()
    ls15_2()
    ls15_3()
    ls15_4()
    ls15_5()
    ls15_6()
    ls15_7()

    print((ls15_8('ls_3.py', 8)))
