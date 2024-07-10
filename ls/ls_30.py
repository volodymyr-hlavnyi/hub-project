# inerators

def ls30_1():
    my_list = [1, 2, 3]
    for item in my_list:
        print(item)
    iterator = iter(my_list)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


def show_letters(some_text):
    for letter in some_text:
        if letter.isalpha():
            print(letter)


def show_letters_gen(some_text):
    # return (letter for letter in some_text if letter.isalpha())
    yield from ''.join([_ for _ in some_text if _.isalpha() or _ == ' '])


def ls30_2():
    need_string = show_letters_gen('Hello, world!')
    for letter in need_string:
        print(letter, end='')

    need_string = show_letters_gen('12345')
    print(need_string)
    print(show_letters_gen(''))


def ls30_3():
    import itertools
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    size = ['S', 'M', 'L']
    for color, size in itertools.product(colors, size):
        print(color, size)


def ls30_4():
    import itertools
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    for item in itertools.chain(list1, list2):
        print(item)


# создаем генератор который
# выполняет то же, что и range
# с одним аргументом
def ls30_6():
    def my_range(stop):
        start = 0
        while start < stop:
            yield start
            start += 1

    def my_range_2(*args):
        stop, start, step = 0, 0, 1

        if len(args) == 1:
            stop = args[0]
        elif len(args) == 2:
            stop = args[1]
            start = args[0]
        elif len(args) == 3:
            step = args[2]
            if step > 0:
                stop = args[1]
                start = args[0]
            else:
                stop = args[0]
                start = args[1]

        if step > 0:
            while start < stop:
                yield start
                start += step
        else:
            while start > stop:
                yield start
                start += step

    print('my_range_2(5) ==')
    for i in my_range_2(5):
        print(i)

    print('my_range_2(5,10) ==')
    for i in my_range_2(5, 10):
        print(i)

    print('my_range_2(5, 10, -1) ==')
    for i in my_range_2(5, 10, -1):
        print(i)

    print('my_range_2(5, 11, -2) ==')
    for i in my_range_2(5, 11, -2):
        print(i)


if __name__ == '__main__':
    # ls30_1()
    ls30_2()
    a = 'asd-90,mn,34m590dsfvndskfjv9cxn sdilkf9 '
    b = [x for x in a if x.isalpha()]
    # print([x for x in a])
    # print(b)
    ls30_3()

    ls30_6()
