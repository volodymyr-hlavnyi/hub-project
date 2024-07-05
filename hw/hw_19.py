# Напишите программу, которая принимает список слов и
# возвращает список, содержащий только анаграммы.
#
#
# Анаграммы - это слова, составленные из одних и тех же букв,
# но в разном порядке.
#
#
# Создайте функцию anagrams, которая принимает список слов в
# качестве аргумента и возвращает список анаграмм.
# Используйте множества и сортировку букв в слове для проверки
# на анаграмму. Выведите результат на экран.
#
#
# Пример переданного списка слов:
#
# ['cat', 'dog', 'tac', 'god', 'act']
#
# Пример вывода:
# Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']


def hw19_1(list_of_words):
    result = []
    word_of_processed = []
    for word in list_of_words:
        check_word = word
        result_list = []
        word_of_processed.append(check_word)
        for word2 in list_of_words:
            if word2 == check_word:
                continue
            if word2 in word_of_processed:
                continue
            if set(check_word).intersection(set(word2)) == set(check_word):
                if not (check_word in result_list):
                    result_list.append(check_word)
                result_list.append(word2)
                word_of_processed.append(word2)

        if result_list:
            result.append(result_list)

    return result


def is_subset(set1, set2):
    flag_all_symbol_is_present = False
    for symbol1 in set1:
        if symbol1 in set2:
            flag_all_symbol_is_present = True
        else:
            flag_all_symbol_is_present = False
            break

    return flag_all_symbol_is_present


a = ['cat', 'dog', 'tac', 'god', 'act', 'bober', 'top']


# def return_anagram_dict(words: list[str]):
#     anagram_dict = dict()
#     words = [(word, ''.join(sorted(list(word)))) for word in words]
#     for item in words:
#         if item[1] not in anagram_dict:
#             anagram_dict.update({item[1]: [item[0]]})
#         else:
#             anagram_dict[item[1]].append(item[0])
#     return [value for value in anagram_dict.values() if len(value) > 1]
#
#     print(return_anagram_dict(a))


if __name__ == '__main__':
    list_of_words = ['cat', 'dog', 'tac', 'god', 'act']
    print(f'Original list: {list_of_words}')
    print(f'Anagrams: {hw19_1(list_of_words)}')

    list_of_words = ['act', 'pin', 'nip', 'cat', 'dog', 'god', 'tac', 'rop', 'por']
    print(f'Original list: {list_of_words}')
    print(f'Anagrams: {hw19_1(list_of_words)}')

    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}
    print(is_subset(set1=set1, set2=set2))
