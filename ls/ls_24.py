def ls_24_1():
    hash_value = hash("hello")
    print(hash_value)  # Выводит целочисленное значение хэша


def ls_24_2():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference = set1.difference(set2)
    symmetric_difference = set1.symmetric_difference(set2)
    print(intersection)  # Выводит {2, 3}
    print(union)  # Выводит {1, 2, 3, 4}
    print(difference)  # Выводит {1}
    print(symmetric_difference)  # Выводит {1, 4}


def ls_24_3():
    words = ['hello', 'daddy', 'hello', 'mum']
    print(words)
    set(words)
    print(set(words))  # Выводит ['hello', 'daddy', 'hello', 'mum']


def ls_24_4(param: str = 'Hello World!'):
    return hash(param)


def ls_24_5():
    set1 = {1, 2, 'a'}
    print(type(set1))  # Выводит <class 'set'>
    print(set1)


def ls_24_6():
    set1 = {}
    print(type(set1))  # Выводит <class 'set'>
    print(set1)


def ls_24_7():
    set1 = set()
    print(type(set1))  # Выводит <class 'set'>
    print(set1)

    try:
        set(1)
    except Exception as e:
        print(f'e.__class__.__name__ = {e.__class__.__name__} {e}')


if __name__ == '__main__':
    ls_24_1()
    ls_24_2()
    ls_24_3()
    print(ls_24_4())
    ls_24_5()
    ls_24_6()
    ls_24_7()
