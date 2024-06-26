def ls17_1():
    a = [1, 2, 3, 4, 5]
    print(id(a), a)
    a[0] = 100
    a.extend([6, 7, 8])
    print(id(a), a)


def ls17_2(my_list):
    for item in my_list:
        print(item, end=' ')


def ls17_3():
    a = [1, 2, 3, 'for', [1, 2]]
    print(a)
    a = [1, 2, 3, 'for', [1, 2]][::-1]
    print(a)


def ls17_4():
    # a = ['apple', 'orange', 'banana', 'kiwi']
    # b = a.split()
    # print(''.b.join())
    pass


def ls17_5(list1):
    uniq_list = []
    for num in list1:
        if num not in uniq_list:
            uniq_list.append(num)
    return uniq_list


def ls17_6(str1):
    print(str)
    list_str = str1.split()
    # print(list_str)
    new_string = list_str[::-1]
    return ' '.join(new_string)


def clear_word(word):
    result = ''
    for char in word:
        if char.isalpha():
            result += char
    return result.lower()


def ls17_7():
    import os
    input_file_path = os.path.join('..', 'files', 'input_text_17.txt')
    words = []
    with open(input_file_path, 'r') as file:
        for line in file:
            words.extend(line.strip().split())
    words = list(map(clear_word, words))
    quantity = []
    for word in words:
        quantity.append(0)

    for word in words:
        quantity[words.index(word)] += 1

    for word, quantity in zip(words, quantity):
        print(word, quantity)


if __name__ == '__main__':
    ls17_1()
    print('----')
    # ls17_2()
    print('----')
    ls17_3()
    print('----')
    ls17_4()
    # list_num = list(map(int, input('Enter list of numbers: ').split()))
    list_num = []
    if len(list_num) == 0:
        list_num = [1, 2, 3, 4, 2, 3, 1, 5]
    print(list_num)
    print(ls17_5(list_num))
    print('----')
    # str1 = input('Enter a string: ')
    str1 = ''
    if len(str1) == 0:
        str1 = 'This is a test string 12 89 !'
    print(ls17_6(str1))
    print(' '.join(str1.split()[::-1]))
    print('----')
    ls17_7()





    # with open('example.txt', 'r', encoding='utf-8') as file:
    #     file_lines = file.readlines()
    #     words = []
    #     for line in file_lines:
    #         words.extend(line.split())
    #     words = list(map(clear_word, words))
    #     quantities = []
    #     for word in words:
    #         quantities.append(0)
    #     for word in words:
    #         quantities[words.index(word)] += 1
    #     for word, quantity in zip(words, quantities):
    #         print(f'{word}: {quantity}')