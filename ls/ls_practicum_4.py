# 1.Дано
# натуральное число N.
# Написать функцию digits_sum(N),
# которая вычисляет сумму его цифр.
# При решении этой задачи пользуемся рекурсией,
# а строки, списки, массивы и циклы не используем.
# Пример digits_sum(179) = 17

def digits_sum(list_num):
    if len(list_num) == 0:
        return 0
    return int(list_num[0]) + int(digits_sum(list_num[1:]))


def pr1_1():
    from collections import defaultdict
    voices = [('McCaln', 10),
              ('McCaln', 5),
              ('Obama', 9),
              ('Obama', 8),
              ('McCaln', 1)]
    for vc in voices:
        print(vc[0], vc[1])

    new_dict = defaultdict(list)

    value_sum = 0
    # for vc in voices:
    #     new_dict[vc[0]].insert(,vc[1])

    print('Result---')
    for key, value in new_dict.items():
        print(key, value)


if __name__ == '__main__':
    # inp_num = input('Enter number: ')
    # print(digits_sum('1234'))

    # pr1_1()
    raw_files = [input("Enter the file name: ") for _ in range(int(input("Enter the number of files: ")))]

    files = {}
    for file in raw_files:
        tmp = file.split()
        files[tmp[0]] = tmp[1:]

    print(files)

    request = [input("Enter the request: ").split() for _ in range(int(input("Enter number request: ")))]
    rights_mapping = {
        "read": "R",
        "write": 'W"',
        "execute": "X"
    }

    for request in request:
        access_type, file_name = request[0], request[1]
        short_exist_type = rights_mapping[access_type]
        if short_exist_type in files[file_name]:
            print("OK")
        else:
            print("Access denied")
# 4
# helloworld.exe R X
# pinglog W R
# nya R
# goodluck X W R
# 5
# read nya
# write helloworld.exe
# execute nya
# read pinglog
# write pinglog