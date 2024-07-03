import time


def hw18_2_non_tail(lst):
    if not lst:
        return 0
    return lst[0] + hw18_2_non_tail(lst[1:])


def hw18_2_tail(lst, acc=0):
    if not lst:
        return acc
    return hw18_2_tail(lst[1:], acc + lst[0])


def test_time_tailand_non_tail_recursion():
    lst = [x for x in range(1, 996)]
    start_time = time.time()
    print(hw18_2_non_tail(lst=lst))
    print(time.time() - start_time)

    start_time = time.time()
    print(hw18_2_tail(lst=lst))
    print(time.time() - start_time)


if __name__ == '__main__':
    # test
    test_time_tailand_non_tail_recursion()
