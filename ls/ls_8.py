# from ls_8_modul import pi
from ls_8_modul import math
from decimal import Decimal, getcontext


def ls8_1():
    return math.pi, math.sqrt(16), math.sin(math.pi / 2)


def ls8_2():
    pass


def ls8_3(a, n):
    s = n * math.pow(a, 2) / (4 * math.tan(math.pi / n))
    return s


def ls8_4():
    number1 = Decimal('0.1')
    number2 = Decimal('0.2')
    return number1 + number2


def ls8_5(int: prec=10):
    getcontext().prec = prec
    number1 = Decimal('1')
    number2 = Decimal('7')
    return number1 / number2


if __name__ == '__main__':
    print('==========')
    print(ls8_1())
    # print(math.round(2.54))
    print(math.ceil(2.54))
    print(math.floor(2.54))
    print(round(2.54))
    print(math.e)
    print(math.log(10))
    print(math.radians(180))
    print(math.degrees(math.pi))
    print(math.fabs(-15))
    # print(pi)
    print(math.pi)
    print('==========')
    # n = int(input("Enter a number n : "))
    # a = float(input("Enter a number a : "))
    # print(ls8_3(n, a))
    print(ls8_4())
    print(ls8_5(3))
    print(ls8_5(10))
