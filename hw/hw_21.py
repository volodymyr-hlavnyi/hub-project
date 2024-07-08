# 1. Напишите программу, которая подсчитывает количество
# вхождений каждого слова в тексте и выводит на экран наиболее
# часто встречающиеся слова. Для решения задачи используйте класс
# Counter из модуля collections. Создайте функцию count_words, которая
# принимает текст в качестве аргумента и возвращает словарь с к
# оличеством вхождений каждого слова. Выведите наиболее часто встречающиеся
# слова и их количество.
#
#
# Пример вывода:
# Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
# sed: 2
# Lorem: 1


def hw21_1_input():
    text_input = input("Enter string: ")
    if text_input == '':
        text_input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est."
        print(text_input)
    return text_input.lower()


def count_words(text_for_count):
    from collections import Counter
    return Counter(text_for_count.split())


def print_fr_word(counter_text_dict, max_words=2):
    list_for_count = [(key, value) for key, value in counter_text_dict.items()]
    list_sorted = sorted(list_for_count, key=lambda item: item[1], reverse=True)
    for word, count in list_sorted[:max_words]:
        print(word, count)


# 2. Напишите программу, которая создает именованный кортеж
# Person для хранения информации о человеке, включающий
# поля name, age и city. Создайте список объектов Person
# и выведите информацию о каждом человеке на экран.
#
#
# Пример вывода:
#
# Name: Alice, Age: 25, City: New York
# Name: Bob, Age: 30, City: London
# Name: Carol, Age: 35, City: Paris

def hw21_2():
    from collections import namedtuple
    Person = namedtuple("Person", ["name", "age", "city"])
    person1 = Person("Alice", 25, "New York")
    person2 = Person("Bob", 30, "London")
    person3 = Person("Carol", 35, "Paris")
    return person1, person2, person3


def get_value_from_dict(dict_input, key, is_use_get):
    if is_use_get == 'y':
        return dict_input.get(key, 'Key not found')
    else:
        try:
            return dict_input[key]
        except KeyError:
            return 'Key not found'


if __name__ == '__main__':
    print('21_1', '*' * 10)
    print_fr_word(count_words(hw21_1_input()), 2)

    print('21_2', '*' * 10)
    my_Persons = hw21_2()
    for person in my_Persons:
        print(f'Name: {person.name}, Age: {person.age}, City: {person.city}')

    print('21_3', '*' * 10)
    my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
    key = input("Enter key for search: ")
    is_use_get = input("Do you want to use get (y/n)? ")
    result = get_value_from_dict(my_dict, key, is_use_get)
    print(f"Value for key '{key}' : {result}")
