def ls3_1():
    x = 5
    y = 2
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x // y)
    print(x % y)
    print(x ** y)


def ls3_2():
    x = 0.1
    y = 0.1
    z = 0.1
    result = x + y + z
    print(result)
    fractional_part = str(result).split('.')[1]
    print(len(fractional_part))


def ls3_3():
    n = input('Enter counts Students: ')
    k = input('Enter counts Apples: ')
    eech_student = int(k) // int(n)
    apples_in_basket = int(k) % int(n)
    print(f'Each St8udent get by {eech_student} apples')
    print(f'Apple in the basket - {apples_in_basket}')


def ls3_4():
    x = 10
    y = 5
    print(x & y)
    print(x | y)
    print(x ^ y)
    print(x << 1)
    print(x >> 1)


def ls3_5():
    x = -5
    y = 5
    print(f'abs - {abs(x)} {abs(y)}')
    print(f'pow - {pow(x, y)} {pow(y, x)}')
    print(f'round - {round(0.006, 2)}')
    print(f'max - {max(x, y)}')
    print(f'min - {min(x, y)}')
    print(f'sum - {sum([x, y])}')


def ls3_6():
    x = 2
    end = 10
    for i in range(x, end + 1):
        print(x)
        x += 1


def ls3_7():
    days = input('Enter days: ')
    hours = input('Enter hours: ')
    minutes = input('Enter minutes: ')
    seconds = input('Enter seconds: ')
    result_seconds = (
            int(days) *
            86400 +
            int(hours) *
            3600 + int(minutes) *
            60 +
            int(seconds))
    print(f'In seconds result is {result_seconds}')


if __name__ == "__main__":
    # ls3_1()  # 7 3 10 2.5 2 1 25
    # ls3_2()  # 0.30000000000000004
    # ls3_3()
    # ls3_4()
    # ls3_5()
    # ls3_6()
    ls3_7()
