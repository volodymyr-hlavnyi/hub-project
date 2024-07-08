import sys


def ls29_1():
    try:
        x = int("abc")
    except ValueError:
        print("Ошибка преобразования строки в число")
    except TypeError:
        print("Ошибка типа данных")


def ls29_2():
    try:
        x = int("abc")
    except Exception:
        print("Какая-то ошибка")
    except ValueError:
        print("Ошибка преобразования строки в число")


def ls29_3():
    try:
        x = int('abc')  # 10 / 0
        print(x)
    except ZeroDivisionError:
        print("Division by zero")
    except Exception as e:
        print(e)


def ls29_4():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    my_class = ZeroDivisionError
    while my_class:
        print(my_class.__name__, end=' -> ')
        try:
            my_class = my_class.__bases__[0]
        except:
            sys.exit()


def ls29_5():
    from collections import defaultdict
    d = defaultdict(list)
    f = []
    with open('ls_29_5.txt', 'r') as f:
        try:
            f = f.readlines()
        except FileNotFoundError:
            print('File not found')
        except Exception as e:
            print(e)

    if f not in [None, []]:
        for line in f:
            print(line)
            line_splited = line.split()
            name = line_splited[1]
            sername = line_splited[0]
            try:
                year = int(line_splited[2])
            except:
                year = 0
            try:
                course = int(line_splited[3])
            except:
                course = 0
            try:
                score = int(line_splited[4])
            except IndexError:
                score = 0
            d[f'{sername}_{name}'].append([name, sername, year, course, score])
    print('Result---')
    for key, value in d.items():
        print(key, value)


def ls29_6(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Деление на ноль")


if __name__ == '__main__':
    # print(1, '*' * 10)
    # ls29_1()
    # print(2, '*' * 10)
    # ls29_2()
    #
    # print(3, '*' * 10)
    # ls29_3()
    #
    # print(4, '*' * 10)
    # ls29_4()

    print(5, '*' * 10)
    ls29_5()

    print(6, '*' * 10)
    ls29_6(2, 0)
