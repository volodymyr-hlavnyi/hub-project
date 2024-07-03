def ls_23_1():
    print(ls_23_1.__name__)
    from functools import partial

    def say(a, b, c='!'):
        print(a, b, c)

    say('Bye', 'Mike')
    say('Hello', 'world', c='.')
    new_say = partial(say, 'Hello', b='Jack')
    new_say()


def ls_23_2():
    print(ls_23_2.__name__)

    def message():
        print('Это рекурсивная функция')
        message()

    message()


def ls_23_3():
    print(ls_23_3.__name__)

    def message(times):
        if times > 0:
            print('Это рекурсивная функция')
            message(times - 1)

    message(5)


def ls_23_4():
    def message(times):
        if times > 0:
            print('Это рекурсивная функция.')
            message(times - 1)
            print(times)

    message(5)


"""Объясните, чем необходимо заменить ... , чтобы получить указанный результат? """


def ls_23_5():
    print(ls_23_5.__name__)

    def sum_items(*args: int):
        print(type(args))
        args_str_lc = [str(arg) for arg in args]

        args_str = map(str, args)
        print(type(map(str, args)))
        print(f"{'+'.join(args_str)}={sum(args)}")

    lst = [1, 2, 3]
    sum_items(*lst)  # 1+2+3=6


"""Дана функция numbers_squared.
Перепишите её как лямбда-функцию numbers_squared_lambda.
"""


def ls_23_6():
    def numbers_squared(lst: list[int]) -> list[int]:
        new_lst = []
        for item in lst:
            new_lst.append(item ** 2)

        return new_lst

    lst = [1, 2, 3]
    print(numbers_squared(lst))  # [1, 4, 9])
    num = lambda lst: [item ** 2 for item in lst]
    num2 = lambda lst: map(lst ** 2, lst)
    # print('num', list(num))
    # print('num2', list(num2))


def ls_23_7():
    from functools import partial
    from typing import Callable

    # Создание новой функции, которая всегда будет использовать аргумент x = 2
    multiply_by_two = partial(lambda x, y: x * y, 2)
    multiply_to_four = partial(lambda x, y: x * y, y=4)

    # print(isinstance(multiply_by_two, Callable))
    print(multiply_by_two(5))  # Выводит 10
    print(multiply_to_four(8))  # Выводит 32


def ls_23_8():
    from functools import partial
    def get_total_cost(price, tax_rate):
        return round(price * (1 + tax_rate), 2)

    get_total_cost_tax_rate_0 = partial(get_total_cost, tax_rate=0)
    get_total_cost_tax_rate_9 = partial(get_total_cost, tax_rate=0.9)
    get_total_cost_tax_rate_20 = partial(get_total_cost, tax_rate=0.20)

    print(get_total_cost_tax_rate_0(100))
    print(get_total_cost_tax_rate_9(109))
    print(get_total_cost_tax_rate_20(120))


def ls_23_9():
    def say(a, b, c='!'):
        print(a, b, c)


def ls_23_10():
    # 1. base
    # 2 Operation
    # 3. Finish
    def countdown(n):
        if n == 0:
            print('Finished!')
        else:
            print(n)
            countdown(n - 1)

    countdown(5)


def ls_23_11():
    def sum_list(lst):
        if not lst:
            return 0
        tmp = lst[0] + sum_list(lst[1:])
        print(f'tmp {id(tmp)} - tmp = {tmp} sum_list -> {id(sum_list)}')
        return tmp

    def sum_list_2(lst):
        return sum(lst)

    print(sum_list([1, 2, 3, 4, 5]))
    print(sum_list_2([1, 2, 3, 4, 5]))

    def sum_list_tall_recursion(lst, acc=0):
        if not lst:
            return acc
        tmp = sum_list_tall_recursion(lst[1:], acc + lst[0])
        return tmp

    print(sum_list_tall_recursion([1, 2, 3, 4, 5]))


def ls_23_12():
    from functools import lru_cache
    @lru_cache
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print(fibonacci(7))


if __name__ == '__main__':
    ls_23_1()
    ls_23_3()
    ls_23_4()
    ls_23_5()
    ls_23_6()
    ls_23_7()
    ls_23_8()
    ls_23_10()
    ls_23_11()
    ls_23_12()


    def sum_tail(lst, acc=0):
        if not lst:
            return acc
        return sum_tail(lst[1:], acc + lst[0])


    def sum_non_tail(lst):
        if not lst:
            return 0
        return lst[0] + sum_non_tail(lst[1:])


    print(sum_tail([1, 2, 3, 4, 5]))
    print(sum_non_tail([1, 2, 3, 4, 5]))
