def ls37_1():
    iterable = ['1', '2', '3']
    result = list(map(len, iterable))
    print(result)


def ls37_2():
    iterable = [[1], [2], [3]]
    result = list(map(len, iterable))
    print(result)


def ls37_3():
    iterable = [1, 2, 3]
    # result = list(map(len, iterable))
    print(result)


def ls37_4():
    import itertools

    letters = ['a', 'b', 'c']
    numbers = [1, 2, 3]
    combinations = list(itertools.combinations(letters, 2))
    print(combinations)
    # Результат: [('a', 'b'), ('a', 'c'), ('b', 'c')]
    permutations = list(itertools.permutations(numbers))
    print(permutations)
    # Результат: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    product = list(itertools.product(letters, numbers))
    print(product)
    # Результат: [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]


def ls37_5():
    from operator import add
    from itertools import accumulate

    result = list(accumulate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], add))
    print(result)


def ls37_6():
    from random import randint
    from functools import reduce

    a = [randint(1, 10) for _ in range(4)]
    print(a)
    print(reduce(lambda x, y: x + y, a))


def ls37_7():
    print(len([333, 2]))
    print('-' * 10)
    iter = [[1], [2], [3]]
    result = list(map(lambda x: len(x), iter))
    print(result)
    result2 = list(map(lambda x: [len(x)], iter))
    print(result2)


def ls37_8():
    import itertools
    letters = ['a', 'b', 'c']
    numbers = [1, 2]
    # zipped = list(itertools.zip_longest(letters, numbers, fillvalue='-'))
    zipped = list(itertools.zip_longest(letters, numbers, fillvalue=0))
    print(zipped)


# ------------------------------

def at_least_one_capital(password: tuple[str]):
    for ch in password:
        if ch.isupper():
            return True
    return False


def is_least_one_num(password: tuple[str]):
    for ch in password:
        if ch.isalnum():
            return True
    return False


def at_least_one_num(password: tuple[str]):
    for ch in password:
        if ch.isnumeric():
            return True
    return False


def at_least_one_lower(password: tuple[str]):
    for ch in password:
        if ch.islower():
            return True
    return False


def is_unique_symbols(password: tuple[str]):
    return len(password) == len(set(password))


def no_neighbour_letters(password: tuple[str]):
    for i in range(len(password) - 1):
        if abs(ord(password[i]) - ord(password[i + 1])) == 1:
            return False
    return True


def ls37_9():
    import random, itertools
    numbers = [str(i) for i in range(0, 10)]
    print(numbers)
    symb_small = [chr(i) for i in range(ord('a'), ord('z'))]
    symb_big = [chr(i) for i in range(ord('A'), ord('Z'))]
    print(symb_small)
    print(symb_big)
    all_symbols = numbers + symb_big + symb_small

    passwords = itertools.permutations(all_symbols, 4)
    rules = [
        at_least_one_lower,
        at_least_one_capital,
        at_least_one_num,
        is_unique_symbols,
        no_neighbour_letters
    ]
    for rule in rules:
        passwords = filter(rule, passwords)

    with open('passwords.txt', 'w', encoding='utf-8') as file:
        for password in passwords:
            file.write(''.join(password) + '\n')


if __name__ == '__main__':
    # ls37_1()
    # ls37_2()
    # ls37_4()
    # ls37_5()
    # ls37_8()
    ls37_9()
