import random


def ls6_1():
    count = 0
    while count < 5:
        print(count)
        count += 1


def ls6_2():
    count = 0
    while count < 10:
        if count == 5:
            break
        print(count)
        count += 1


def ls6_3():
    count = 0
    while count < 10:
        count += 2
        if count == 3:
            continue
        print(count)


def ls6_4():
    import time
    start_time = time.time()
    count = 0
    while count < 100:
        count += 1
        if count == 3:
            continue
        print(count)
    else:
        print(f'Done count = {count}')
    print(time.time() - start_time)


def ls6_5():
    c = 1
    while True:
        num = input('Enter number: ')
        if num == 'exit':
            break
        print(int(num) ** 2)


def ls6_6():

    pass


def ls6_7():
    my_list = ['cherry', 'apple', 'banana', 'kiwi', 'apple', 'banana']
    print(random.choice(my_list))
    print(random.randrange(1, 10))
    print(random.random())
    random.shuffle(my_list)
    print(my_list)


if __name__ == '__main__':
    ls6_1()
    print('----')
    ls6_2()
    print('----')
    ls6_3()
    print('----')
    ls6_4()
    print('----')
    # ls6_5()
    print('----')
    ls6_6()
    print('----')
    ls6_7()
