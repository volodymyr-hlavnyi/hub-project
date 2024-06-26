def ls_1(num, pw):
    for i in range(1, pw + 1):
        print(num, "**", i, "=", num ** i)


def ls_2(x, y, z):
    sum = x + y + z
    return sum


def ls_3(hour, minut, second):
    # import datetime
    # dif_hour = (
    #     datetime.timedelta(hours=hour, minutes=minut, seconds=second))
    pass


def ls_4(a, b):
    if a > b:
        return f'{a} > {b} -> {a}'
    elif a < b:
        return f'{a} < {b} -> {b}'
    else:
        return f'{a} = {b} -> {a} = {b}'


# Найти наибольшее из трех чисел
def ls_5(a, b, c):
    if a > b:
        if a > c:
            return f'max a -> {a}'
        else:
            return f'max c -> {c}'
    else:
        if b > c:
            return f'max b -> {b}'
        else:
            return f'max c -> {c}'


def ls_6(weekday):
    return 'WeekDay' if weekday else 'WeekEnd'


def ls_7(isWeekDay, isVacation):
    return \
        'Can more sleeping...' \
            if not isWeekDay and isVacation \
            else 'Go to work...'


def ls_8(num):
    count = 0
    i = 0
    while i <= num:
        if i % 2 == 0:
            count += 1
        i += 1
    return count


if __name__ == '__main__':
    # ls_1(5, 3)
    print('==============')
    # ls_1(4, 8)
    # print(ls_2(0.1,0.2,0.3))
    # print('==============')
    # print(ls_3(9, 45 , 00))
    # print('==============')
    # a = int(input('a: '))
    # b = int(input('b: '))
    # print(ls_4(a, b))
    # print('==============')
    # a = int(input('a: '))
    # b = int(input('b: '))
    # c = int(input('c: '))
    # print(ls_5(a, b, c))
    # print(ls_6(False))
    # print(ls_6(True))
    # print('==============')
    # print(ls_7(False, True))
    print('==============')
    num = int(input('N: '))
    print(ls_8(num= num))
