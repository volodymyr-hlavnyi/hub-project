from random import randint

list1 = [randint(1, 21) for i in range(10)]

list2 = [x ** 2 for x in list1]

print(list1)
print(list2)


def sum_digit(num):
    print(f'num {num}')
    if abs(num) < 10:
        return num
    demo1 = num % 10
    demo2 = num // 10
    print(demo1, demo2)
    return num % 10 + sum_digit(num // 10)


print(f'sum_digit = {sum_digit(12345)}')
print(f'sum_digit = {sum_digit(12345)}')

print(sum(map(int, '12345')))
num1_str = '545489'
print(num1_str)
print(len(set(map(int, num1_str))))

