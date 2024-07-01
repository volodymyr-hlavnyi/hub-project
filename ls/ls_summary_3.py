def ls_sm_3():
    a = [chr(i) for i in range(97, 123)]
    b = [ord(i) for i in a]
    print(a)
    print(b)
    print(type(zip(a, b)))
    print(*zip(a, b))


def ls_sm_2():
    with open('../files/input_text_17.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


def ls_sm_3(string_for_print='Python is awesome!'):
    print()
    print(f'{string_for_print}\n' * 10)


def ls_sm_4():
    def print_line():
        print('*' * 10)

    def print_line_2():
        print('*', ' ' * 8, '*', sep='')

    print_line()
    for i in range(1, 13):
        print_line_2()
    print_line()


def ls_sm_5():
    new_list = []
    for i in range(97, 123):
        new_list.append(chr(i) * (i - 96))
    return new_list


def ls_sm_6():
    my_list = [1, 2, 3]
    my_list.insert(2, 5)
    print(my_list)


def ls_sm_7():
    my_list = ['1', '2', '3']
    my_list.insert(2, 5)
    print(my_list)


def ls_sm_8():
    my_list_a = [i for i in range(0, 6)]
    my_list_b = [chr(k) for k in range(97, 103)]
    print(my_list_a, '\n', my_list_b)
    my_list_c = zip(my_list_a, my_list_b)
    print(list(*my_list_c))
    for key, value in enumerate(list(my_list_c)):
        print(key, value)



if __name__ == '__main__':
    ls_sm_3()
    ls_sm_2()
    ls_sm_3()
    ls_sm_4()
    print(ls_sm_5())
    ls_sm_6()
    ls_sm_7()
    ls_sm_8()
