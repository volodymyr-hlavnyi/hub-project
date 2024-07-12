def my_generator():
    i = 0
    while True:
        yield i
        i += 1


def my_generator_2():
    rec = yield 1
    while True:
        rec = yield rec * 2


def my_gen_3():
    try:
        yield 'start_outer'
        yield from (i for i in range(3))
        yield 'end_outer'
    except GeneratorExit:
        print('run cleaup workflow')
    except ZeroDivisionError:
        print('manualy executed exception')


# gen = my_generator_2()
# print(gen.send(None), 1, "None")
# print(gen.send(20), 2, "20")
# print(gen.send(100), 3, "100")
# print(gen.send(1500), 4, "1500")
# print(next(gen), 5, "next")

gen = my_gen_3()
for i in gen:
    if i == 2:
        gen.close()
    print(i)


# gen = my_gen_3()
# for i in gen:
#     if i == 2:
#         gen.throw(ZeroDivisionError)

def sum_rec(n: int):
    print(f"sum_rec({n})")
    if n == 1:
        return n
    else:
        return n + sum_rec(n - 1)

print("sum_rec")
print(sum_rec(5))

a = dict()
a.update({1:'234'})
a.update({3:'texdr'})
print(a)
print(a.get(1))
for key, value in a.items():
    print(key, value)


print(ZeroDivisionError.__base__.__base__.__base__)

my_gen=(x for x in range(10))
for item in my_gen:
    print(item)