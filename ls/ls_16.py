def ls16_1(user_name):
    print(f'Hello, {user_name}.')


def ls16_2(a: str = 'tom'):
    return f'Hello, {a}. Your string len is {len(a)}.'


def double(number):
    return number * 2


def ls16_3():
    result1 = double(4)
    result2 = double(10)
    print(f'result1 = {result1}')
    print(f'result2 = {result2}')


def ls16_4():
    global a
    print(a)
    a = 6
    print(a)


def ls16_5():
    b = 45
    return b


def smth():
    i = 100
    print(i)


def ls16_6(str1='Apple', str2='Samsung'):
    return len(f'{str1}{str2}')


def ls16_7():
    i = 1
    for j in range(10):
        if i % 2 == 0:
            print(i)
        else:
            smth()
        i += 1


def greet_person(*args, **kwargs):
    print(args)
    print(kwargs)


def ls16_8(list_numbers):
    def check_num_3_or_5(num1):
        if num % 3 == 0 or num % 5 == 0:
            return True
        else:
            return False

    num_len = len(list_numbers)
    sum_num = 0
    for num in list_numbers:
        if check_num_3_or_5(num):
            sum_num += num
    return sum_num


if __name__ == '__main__':
    ls16_1('Mark')
    ls16_1('Duran')
    print(ls16_2('Tom'))
    print(ls16_2('National Geographic'))
    ls16_3()
    a = 10
    ls16_4()
    print(a)
    ls16_5()
    print('-----')
    ls16_7()
    print('-----')
    print(ls16_6())
    print('-----')

    greet_person('Mark', 'Duran', age=25, city='New York')

    print('-----')
    sum_3_or_5_1 = ls16_8([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 45])
    sum_3_or_5_2 = ls16_8([1, 2, 3])

    print(f'Sum (3 or 5 div): {sum_3_or_5_1}')
    print(f'Sum (3 or 5 div): {sum_3_or_5_2}')
