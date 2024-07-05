def ls25_1():
    my_set = {1, 4}
    my_set.add(4)
    print(my_set)
    set2 = {x for x in range(1, 10)}
    set3 = {x for x in range(6, 10)}
    print(set2)
    print(set3)
    print(set2 or set3)


if __name__ == '__main__':
    ls25_1()
