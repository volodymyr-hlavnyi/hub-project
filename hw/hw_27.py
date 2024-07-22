from functools import reduce


def get_sum_list(numbers: list):
    list1 = filter(lambda x: x % 2 == 0, numbers)
    list2 = map(lambda x: x ** 2, list1)
    return reduce(lambda x, y: x + y, list2)


def hw27_1():
    my_list_str = input("Enter numbers (use ,): ").split(',')
    my_list = list(map(lambda x: int(x), my_list_str))
    return f"Sum odd **2 is : {get_sum_list(my_list)}"


def hw27_2():
    def compose_functions(functions: list, x: int):
        x_list = [x]
        for funct in functions:
            result = list(map(funct, x_list))
            x_list = []
            x_list.append(result[0])
        return x_list[0]

    add_one = lambda x: x + 1
    double = lambda x: x * 2
    subtract_three = lambda x: x - 3
    functions = [add_one, double, subtract_three]
    return compose_functions(functions, 5)


if __name__ == '__main__':

    print(hw27_1())

    print(hw27_2())
