def ls9_1(text: str = 'Hello, World!'):
    return f'{text} {text}'


def ls9_2():
    print('Text1')
    print('John\'s mothers said "No"')
    print("John's mothers said \"No\"")
    print("""John's mothers said "No" """)
    print('"Khal Drogo\'s favorite word is "athjahakar""')


def ls9_3():
    print(str(1 / 7))
    print(float(str(1 / 7)))


def ls9_4(a, b):
    return f'{a} {b}'


def ls9_5(max_symbol: int = 55279):
    for i in range(0, max_symbol):
        if i % 25 == 0:
            print(' ')
            print(f'{i} -', end=' ')
        print(f'{chr(i)}', end=' ')
    print('')


def ls9_6(input_string: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
    for i in input_string:
        print(f'{i} - {ord(i)}')


if __name__ == '__main__':
    print(ls9_1())
ls9_2()
ls9_3()
print('Hello', 'word!')
print(len(ls9_4('Hello', 'word!')))
print(len(ls9_4('Hello', '')))
# ls9_5()
ls9_6()

# print(ord('😀'))
