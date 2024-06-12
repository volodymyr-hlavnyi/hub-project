def ls4_1(a, b, c):
    if a == b == c:
        return True
    else:
        return False


if __name__ == '__main__':

    if ls4_1(1, 1, 1):
        print('Numbers is equal')
    else:
        print('Numbers is not equal')

    if ls4_1(5, 10, 5):
        print('Numbers is equal')
    else:
        print('Numbers is not equal')

    if ls4_1(4, 5, 6):
        print('Numbers is equal')
    else:
        print('Numbers is not equal')
