from typing import Optional, Union, Any
from typing import Iterable


def ls32_1(x: int = 0) -> int:
    return x ** 2


def word_add(string1: str, count: int) -> str:
    return string1 * count


def greet(name: str | None) -> Union[str, int]:
    if name is None:
        return 'Hello anonymous'
    else:
        return f'Hello {name}'


def generate_numbers(n: int) -> Iterable[int]:
    for i in range(n):
        yield i


def my_sorted_data(data):
    from operator import itemgetter
    return sorted(data, key=itemgetter('age'))


def oper(num1: int, num2: int, oper: str):
    import operator
    action = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul,
        "**": operator.pow
    }
    operation = action[oper]
    return operation(num1, num2)


def binary_1():
    from bisect import bisect_left, bisect_right
    data1 = [1, 3, 5, 7, 9]
    data2 = [1, 3, 6, 7, 9]
    index = bisect_left(data1, 6)  # Результат: 3
    print(index)
    index = bisect_right(data1, 6)  # Результат: 3
    print(index)
    index = bisect_left(data2, 6)  # Результат: 2
    print(index)
    index = bisect_right(data2, 6)  # Результат: 3
    print(index)


def ls31_5():
    from bisect import bisect_left, bisect_right
    def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect_right(breakpoints, score)
        return grades[i]

    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])


def ls31_6(list_for_search_max: list[str]) -> str:
    return max(list_for_search_max, key=lambda s: len(s))


def list_str(a: list[str]) -> str:
    return max(a, key=lambda s: len(s))


# print(list_str(['hello', 'mamanja', 'mia']))

# Напишите функцию, которая принимает список
# словарей и ключ, по которому нужно
# отсортировать список словарей.
# Функция должна быть аннотирована с помощью
# аннотаций типов.
def my_sort_dict(n_dict:list[dict], key: Any) -> list[dict]:
    from operator import itemgetter
    # return sorted(n_dict, key=itemgetter(key))
    return sorted(n_dict, key=lambda d: d[key])


if __name__ == '__main__':
    print(ls32_1())
    print(ls32_1(5))
    print(ls32_1(10))
    print(word_add("python", 2))
    print(greet(None))
    print(greet('Volodymyr'))

    a: list[int] = [1, 2, 3, 4]
    b: tuple[str, ...] = ('2', '3')
    # c: set(int | str) = {1, '2'}
    gen = generate_numbers(5)
    for x in range(5):
        print(next(gen))
    data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 20},
        {'name': 'Charli', 'age': 19},
    ]

    for d in my_sorted_data(data):
        print(d)

    # line = input("Enter expression: ").split()
    line = ["5", "*", "9"]
    print(oper(int(line[0]), int(line[2]), line[1]))

    ls31_5()

    from bisect import bisect_left, bisect_right

    data1 = [1, 3, 5, 7, 9, 10, 11, 15]
    data2 = [1, 3, 6, 7, 9]
    index = bisect_left(data1, 12)  # Результат: 3
    print(f"bisect_left {12} {index}")
    index = bisect_right(data1, 12)
    print(f"bisect_rigth {12} {index}")  # Результат: 3
    print(index)

    my_list = [
        'fsdfsdfsdf',
        'fsdf',
        '932n4jk39205u',
        'mrnm,gdfn'
    ]
    print(f"Max str is : {ls31_6(my_list)}")

    n_dict = [
        {'age': 15, 'name': 'Victor'},
        {'age': 10, 'name': 'Ann'},
        {'age': 23, 'name': 'Mike'},
    ]
    print(my_sort_dict(n_dict, 'age'))
    print(my_sort_dict(n_dict, 'name'))
