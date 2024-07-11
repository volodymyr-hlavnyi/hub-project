# 1. Напишите генератор, который будет принимать на вход числа и возвращать их сумму. Генератор должен использовать инструкцию yield для возврата текущей суммы и должен продолжать принимать новые числа для добавления к сумме. Если генератор получает на вход число 0, он должен прекращать работу и вернуть окончательную сумму. Напишите программу, которая будет использовать этот генератор для пошагового расчета суммы чисел, вводимых пользователем.

def cal_sum(x: int = 0):
    s = 0
    while True:
        n = yield s
        if n == 0:
            return s
        s += n


def hw24_1():
    calc_sum_prev = 0
    gen = cal_sum()
    next(gen)
    while True:
        num = int(input("Enter number for sum (0 for finish): "))
        try:
            calc_sum = gen.send(num)
            calc_sum_prev = calc_sum
        except StopIteration:
            calc_sum = calc_sum_prev
            print(f"Current the sum: {calc_sum}")
            break
        print(f"Current the sum: {calc_sum}")


def generate_arithmetic_progression(a1: int, d: int, n: int):
    item = a1
    for _ in range(n):
        yield item
        item += d


if __name__ == '__main__':

    print('\n24_1', '==' * 10)
    hw24_1()

    print('\n24_2', '==' * 10)
    a1 = 1
    d = 1
    n = 10
    gen = generate_arithmetic_progression(a1, d, n)
    for ar in gen:
        print(ar)
