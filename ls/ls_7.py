def ls7_1():
    print(0.1 + 0.1 + 0.01 == 0.3)
    print(0.1 + 0.1 + 0.1)
    a = int(round((0.1 + 0.1 + 0.1) * 10, 2))
    a12 = bin(a)
    print(a12)

    b12 = int(a12, 2)
    print(b12)
    # print(bin(3.14))


def convert_float_to_ieee_standard():
    import struct
    num = float(input('Entery number for convertion to IEEE: '))
    package = struct.pack('>f', num)
    binary_str = ''.join(f'{byte:08b}' for byte in package)
    print(f'Number {num} in binary IEEE format is {binary_str}')


def ls7_2():
    num = int(input('Enter number: '))
    s = ''
    while num:
        s += str(num % 2)
        num //= 2
    print(s)
    i = len(s)
    s1 = ''
    while i:
        s1 += s[i - 1]
        i -= 1
    print(s1)


def ls7_3():
    sum = 0
    for i in range(101):
        # print(i, sum)
        sum += i
    return sum


def ls7_4():
    sum = 0
    for i in range(101):
        if i % 3 == 0:
            sum += i
    return sum


def ls7_5():
    sum = 0
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
    return sum


def ls7_6():
    sum = 0
    for i in range(101):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    # ls7_1()
    # convert_float_to_ieee_standard()
    # print(bin(123))
    # ls7_2()
    print(f'1. {ls7_3()}')
    print(f'2. {ls7_4()}')
    print(f'3. {ls7_5()}')
    print(f'4. {ls7_6()}')
