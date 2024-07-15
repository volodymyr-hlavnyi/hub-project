def ls35_1():
    numbers = [1, 2, 3, 4, 5]
    is_all_positive = all(num > 0 for num in numbers)
    print(is_all_positive)
    any_true = any(num < 0 for num in numbers)
    print(any_true)


def ls35_2():
    item_list = []
    print(all(item_list))


def ls35_3():
    numb = [22, 10, 5, 34, 29]
    print(list(reversed(numb)))


def ls35_4():
    numb = [22, 10, 5, 34, 29]
    for key, value in enumerate(numb):
        print(key, value)


def ls35_5():
    numbers = [1, 2, 3, 4, 5]
    sq = map(lambda x: x ** 2, numbers)
    print(list(sq))
    even = filter(lambda x: x % 2 == 0, numbers)
    print(list(even))


def ls35_6():
    from functools import reduce
    numbers = [1, 2, 3, 4, 5]
    sum = reduce(lambda x, y: x + y, numbers)
    print(sum)


def ls35_7():
    import random
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(numbers)
    more_50 = filter(lambda x: x > 50, numbers)
    print(list(more_50))


def ls35_8():
    print('ls35_8')
    import random
    from functools import reduce
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(numbers)
    reduce_num = reduce(lambda x, y: x + y, numbers)
    print(reduce_num)


def ls35_9():
    print('ls35_9')
    from functools import reduce
    my_string = 'Some string with spaces'
    print(my_string)
    reduce_str = reduce(lambda x, y: x + '|' + y, my_string)
    map_string = map(lambda x: x + '|', my_string)
    print(reduce_str)
    print(''.join(s for s in map_string))


def ls35_10():
    import random
    from functools import reduce
    class Student:
        def __init__(self):
            self.name = ''.join([random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(random.randint(5, 8))])
            self.grade = random.randint(0, 100)

    students = [Student() for i in range(3)]

    for student in students:
        print(student.name, student.grade)

    print(reduce(lambda g, ns: g + ns.grade, students, 0))

def ls35_11():
    with open('anna-karenina.txt', 'r') as input_file:
        input_text = input_file.readline()
        output_file1 = map(lambda x: x.lower(), input_text.split())
        output_file2 = map(lambda x: x.strip(')(,./1234567890!?;[]'), output_file1)
        output_file3 = list(filter(lambda x: len(x)>10, output_file2))
    for line in output_file3:
        print(line)
    print(len(list(output_file3)))


if __name__ == '__main__':
    # ls35_1()
    # ls35_2()
    # ls35_3()
    # ls35_4()
    # ls35_5()
    # ls35_6()
    # ls35_7()
    # ls35_8()
    # ls35_9()
    # ls35_10()
    ls35_11()
