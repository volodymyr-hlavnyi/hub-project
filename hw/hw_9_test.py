# Check speed for operator + and speed operator f-string
# for many values string
import time
import random
import string


def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def test_speed(length_string: int = 100000):
    start = time.time()
    for i in range(length_string):
        a = random_string(10) + ' ' + random_string(10) + ' ' + random_string(10)
    time_plus = time.time() - start
    print('Time for operator +:', time_plus)

    start = time.time()
    for i in range(length_string):
        a = f'{random_string(10)} {random_string(10)} {random_string(10)}'
    time_fstring = time.time() - start
    print('Time for operator f-string:', time_fstring)
    print(' -> ', (time_plus - time_fstring))


if __name__ == '__main__':
    test_number = 1
    for i in range(0, 30, 10):
        real_length = i * 100000
        print(f'test {test_number}: For string length of {real_length}')
        test_speed(real_length)
        test_number += 1
