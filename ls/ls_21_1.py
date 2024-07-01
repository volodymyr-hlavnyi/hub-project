def collector():
    i = 0

    def collect(n):
        nonlocal i
        i += n
        return i

    return collect


collect = collector()
for j in range(10):
    print(collect(j))
print(collect(0))


def def1():
    var1 = 10

    def def2():
        nonlocal var1
        var1 = 20

    def2()
    print(var1)


if __name__ == '__main__':
    def1()
    print('Done')
