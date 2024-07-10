def ls31_1():
    def my_generator():
        try:
            yield 1
            yield 2
            yield 3
        except GeneratorExit:
            pass

    gen = my_generator()
    print(next(gen))
    if next(gen) > 3:
        gen.throw(ValueError("Enough"))


def ls31_2():
    def my_generator():
        try:
            yield 1
            yield 2
            yield 3
        except GeneratorExit:
            pass

    gen = my_generator()
    print(next(gen))
    gen.close()


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def my_generator_2():
    received_value = yield 1
    yield received_value + 1


def test():
    s = 0
    while True:
        x = yield s
        s += x


def my_gen_3():
    value = yield
    if value > 0:
        yield value * 2
    else:
        yield value * 3


def ls31_3():
    def sub_generator():
        yield 'Sub generator'
        yield 'Completed sub generator'

    def main_generator():
        yield 'Main generator'
        yield from sub_generator()
        yield 'Completed main generator'

    gen = main_generator()
    for item in gen:
        print(item)


def set_gen(iterable):
    yield from set(iterable)


if __name__ == '__main__':
    print('31_1', '*' * 10)
    ls31_1()

    print('31_2', '*' * 10)
    ls31_2()

    print('31_3', '*' * 10)
    fib_gen = fibonacci_generator()
    for i in range(20):
        print(next(fib_gen))
    fib_gen.close()

    gen = my_generator_2()
    print(next(gen))
    print(gen.send(10))
    # print(next(gen))

    t = test()
    print(next(t))
    print(t.send(111))
    print(t.send(123))

    t.close()
    t = test()
    print(next(t))

    # gen = my_gen_3()
    # print(next(gen))
    # print(gen.send(5))
    # print(gen.send(-2))

    ls31_3()

    gen = set_gen([4, 2, 1, 2, 1])
    for item in gen:
        print(item)
