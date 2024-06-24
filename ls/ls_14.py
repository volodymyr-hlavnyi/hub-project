# Strings and formating

def ls14_1():
    a = 'hello for me'
    # print(a.split().join(' '))
    print('\n'.join(a.split()))


def ls14_2():
    a = 'hello {}, is it {} you looking for'.format('Student', 'pineapple')
    print(a)


def ls14_3():
    a = 'hello {age}, is it {name} you looking for'.format(age=25, name='John')
    print(a)


def ls14_4():
    a = ('hello {age}, {name}, you '
         'looking for, '
         'balance: ${:8.2f}').format(4587.365, age=25, name='John')
    print(a)
    a = ('hello {age}, {name}, you '
         'looking for, '
         'balance: ${:8.4f}').format(4587.365, age=25, name='John')
    print(a)
    a = 'bin: {:b}, oct: {:o}, hex: {:x}'.format(12, 12, 12)
    print(a)


def ls14_5():
    a = "{:{fill}{align}{width}}"
    print(a.format('cat', fill='*',
                   align='^',
                   width=20))
    a = "{:{fill}{align}{width}.{precision}f}"
    print(a.format(12365.458,
                   fill='_',
                   align='<',
                   width=20,
                   precision=2))
    print(a.format(12365.458,
                   fill='_',
                   align='>',
                   width=20,
                   precision=2))
    print(a.format(12365.458,
                   fill='_',
                   align='^',
                   width=20,
                   precision=2))


def ls14_6():
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    string_name = 'Hello, {name}, you are {age} years old.'
    print(string_name.format(name=name, age=age))


def ls14_7():
    a = 158.456789
    b = 'string'
    print('Number is : %.2f - string is : %s' % (a, b))


def ls14_8():
    from math import pi
    a = input('Enter your age: ')
    b = input('Enter your name: ')
    c = 157.235
    print(f'Hi {b}, your age is {a}, balance is : {c:.2f}.')
    print(f'Pi is {pi:.4f}')


def ls14_9():
    name = 'Jogn Voldjf Fg vjgh VB'
    age = 25
    text = f'{name:>10} is {age:=^10} years old.'
    print(text)


def ls14_10(string_param, avg_m, avg_f, count_m, count_f):
    param = string_param.split('-')
    # print(param)
    if param[2].lower() == 'm':
        avg_m += (int(param[3]) / count_m)
        count_m += 1
    else:
        avg_f += (int(param[3]) / count_f)
        count_f += 1

    return avg_m, avg_f, count_m, count_f


if __name__ == '__main__':
    ls14_1()
    ls14_2()
    ls14_3()
    ls14_4()
    ls14_5()
    # ls14_6()
    ls14_7()
    # ls14_8()
    ls14_9()
    a = ['John-Brown-M-25',
         'Yemili-Brown-F-20',
         'John-Brown-M-25',
         'John-Brown-M-50',
         'Yemili-Brown-F-40', ]
    count_f = 1
    count_m = 1
    avg_m = 0
    avg_f = 0
    for line in a:
        # a = input('Enter string to split: ')
        avg_m, avg_f, count_m, count_f = ls14_10(line, avg_m, avg_f, count_m, count_f)

    print(f'M (avg): {avg_m}, F (avg) {avg_f}, '
          f'\nM (count): {count_m}, F (count): {count_f}')
    # f', count_m, count_f)
