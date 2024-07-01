def ls20_1():
    print(ls20_1.__name__)
    numbers = (0, 1, 3, 14, 2, 7, 9, 8, 10)
    print(numbers)


def ls20_2():
    print(ls20_2.__name__)
    numbers = [0, 1, 3, 14, 2, 7, 9, 8, 10]
    numbers_sq_1 = [numbers[i] ** 2 for i in range(9)]
    numbers_sq = [num ** 2 for num in numbers]
    print(numbers)
    print(numbers_sq)


def ls20_3():
    print(ls20_3.__name__)
    a = (3, [5, 3], 7, [[9, 2], [1, 2, 3]])
    print(len(a))


def ls20_4():
    print(ls20_4.__name__)  # ls20_6
    numbers = (0, 1, 3, 14, 2, 7, 9, 8, 10)
    print(type(numbers))
    # print(numbers[3][1])


def ls20_5():
    print(ls20_5.__name__)  # ls20_6
    numbers = [0, 1, 3, 14, 2, 7, 9, 8, 10]
    print(numbers)
    new = [20, 30]
    numbers.append(new)
    print(type(numbers), numbers)
    print(f'new.pop() {new.pop()}')
    print(new)
    print(numbers)
    numbers.pop()
    print(numbers)


def ls20_6():
    from collections import deque
    # Need to print bame of def
    print(ls20_6.__name__)  # ls20_6
    queue = deque()
    queue.append(1)  # Добавление элемента в очередь
    queue.append(2)
    queue.append(3)
    print(type(queue), queue)
    first_element = queue.popleft()  # Извлечение первого элемента из очереди
    print(first_element)  # 1
    last_element = queue.pop()  # Извлечение последнего элемента из очереди
    print(last_element)


def ls20_7():
    print(ls20_7.__name__)
    a = ['beta', 'alpha', 'gamma', 'delta']
    a.sort()
    print('Sorted list:', a)


def ls20_8():
    import random
    print(ls20_8.__name__)
    numbers = [random.randint(1, 10) for x in range(1, 11)]
    print(numbers)
    numbers.sort(reverse=True)
    print(numbers)


def ls20_9():
    import random
    print(ls20_9.__name__)
    numbers = [random.randint(1, 10) for x in range(1, 11)]
    print(numbers)
    b = []
    for x in range(len(numbers)):
        element = min(numbers)
        b.append(element)
        numbers.remove(element)
    print(b)


def ls20_10():
    import random
    print(ls20_10.__name__)
    numbers = [random.randint(1, 20) for x in range(1, 8)]
    print(numbers)
    b = []
    is_sorted = True
    for j in range(len(numbers)):
        for x in range(len(numbers)-1):
            if numbers[x] > numbers[x+1]:
                numbers[x], numbers[x+1] = numbers[x+1], numbers[x]
                is_sorted = False
            print(numbers)
        print()
        if is_sorted:
            break
    print('Final:')
    print(numbers)


if __name__ == '__main__':
    ls20_1()
    ls20_2()
    ls20_3()
    ls20_4()
    ls20_5()
    ls20_6()
    ls20_7()
    ls20_8()
    ls20_9()
    ls20_10()
