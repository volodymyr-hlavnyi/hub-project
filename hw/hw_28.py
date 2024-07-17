# Напишите программу, которая принимает список слов от пользователя
# и использует генераторное выражение (comprehension) для создания нового списка,
# содержащего только те слова, которые начинаются с гласной буквы.
#
# Затем программа должна использовать функцию map, чтобы преобразовать
# каждое слово в верхний регистр.
# В результате программа должна вывести новый список, содержащий только слова,
# начинающиеся с гласной буквы и записанные в верхнем регистре.

def hw28_1(str4conv: str) -> str:
    new_line2 = list(filter(lambda w: w[0:1].lower() in 'eyuioaуеыаоэяию', [w for w in str4conv.split()]))
    return ' '.join(list(map(lambda w: f'{w[0:1].upper()}{w[1:]}', new_line2)))


def hw28_2(str_numbers: str):
    from functools import reduce
    from itertools import accumulate
    import operator

    list2 = list(map(int, str_numbers.split()))
    prod = reduce(lambda x, y: x * y, list2)
    prod_acc = accumulate(list2, operator.mul)
    return list(prod_acc)


if __name__ == '__main__':
    print('hw 28.1')
    input_str = input('Enter list of words: ')
    # input_str = 'edf ghtyio Opppa Nwdmd dfjghfdjkg Улки палки лес густой Если тогда уль'
    print(hw28_1(input_str))

    print('hw 28.2')
    input_numbers = input("Enter list of numbers (divider 'space' ) : ")
    # input_numbers = '1 3 6 10 20'
    print(hw28_2(input_numbers))
