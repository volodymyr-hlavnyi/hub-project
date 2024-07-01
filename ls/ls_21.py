def ls21_1():
    print(ls21_1.__name__)

    def square(x):
        return x ** 2

    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    squared_numbers = map(square, numbers)
    print(*squared_numbers)


def ls21_2():
    print(ls21_2.__name__)
    numbers = [1, 2, 3, 4, 5]
    numbers_sq = map(lambda x: x ** 2, numbers)
    print(*numbers_sq)


def ls21_3(*args):
    print(ls21_3.__name__)
    for arg in args:
        print(*arg, end='')


def ls21_4_get_min(*args):
    print(ls21_4_get_min.__name__)
    min_num = args[0]
    for x in range(len(args)):
        if args[x] < min_num:
            min_num = args[x]
    return min_num


def ls21_5_get_min(*args):
    print(ls21_5_get_min.__name__)
    return min(args)


def ls21_6_get_min(*args):
    print(ls21_6_get_min.__name__)
    return min(*args)


if __name__ == '__main__':
    import time
    import random

    # ls21_1()
    # ls21_2()
    # ls21_3([1, 2], [34, 9])
    # print(ls21_4_get_min(3, 10, 22, -3, 0))
    # print(ls21_5_get_min(3, 10, 22, -3, 0))
    # a = [random.randint(-1000, 1000) for x in range(0, 10000)]
    # start = time.time()
    # print(ls21_5_get_min(a))
    # time_plus = time.time() - start
    # print(f'Diff time args is : {time_plus}')
    #
    # start = time.time()
    # print(ls21_6_get_min(a))
    # time_plus = time.time() - start
    # print(f'Diff time *args is : {time_plus}')
    people = [('John', 18),
              ('Alice', 23),
              ('Bob', 30),
              ('Anna', 25),
              ('Alex', 20)]
    people.sort(key=lambda person: person[0], reverse=False)
    for person in people:
        print(person)

    print('----')
    people = [('John', 18),
              ('Alice', 23),
              ('Bob', 30),
              ('Anna', 25),
              ('Alex', 20)]
    people_sort = sorted(people, key = lambda person: person[0])
    for person in people:
        print(person)

    print('----')
    name_lenght = [len(person[0]) for person in people]
    print(name_lenght)

