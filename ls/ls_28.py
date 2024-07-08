from functools import lru_cache


def ls28_1():
    my_dict = {"apple": 5, "banana": 2, "orange": 8}
    print(my_dict.get("apple"))  # Выводит 5
    print(my_dict.get("grape"))  # Выводит None
    print(my_dict.get("grape", 0))  # Выводит 0, так как клĀча "grape" нет в словаре


def ls28_2():
    my_dict = {"apple": 5, "banana": 2, "orange": 8}
    print(my_dict.setdefault("apple", 10))  # Выводит 5
    print(my_dict.setdefault("grape", 15))  # Выводит 15, добавлāет новуĀ пару клĀч-значение
    print(my_dict)  # Выводит {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 15}


def ls28_3():
    dct = {
        'a': 'b',
        'b': 'c',
        'c': 'a'}
    print(dct.get('a'))


def ls28_4():
    from collections import OrderedDict
    ordered_dict = OrderedDict()
    ordered_dict["orange"] = 8
    ordered_dict["apple"] = 5
    ordered_dict["banana"] = 2
    print(ordered_dict)

    dict1 = dict()
    dict1["orange"] = 8
    dict1["apple"] = 5
    dict1["banana"] = 2
    print(dict1)


def ls28_5():
    from collections import OrderedDict
    def lru_cache(capacity, cache, key, value):
        if key in cache:
            # Если клĀч уже существует, обновлāем значение и перемещаем ÿлемент в конец словарā
            cache.pop(key)
        elif len(cache) >= capacity:
            # Если кÿш переполнен, удалāем первый ÿлемент (самый старый)
            cache.popitem(last=False)
        cache[key] = value

    capacity = 3
    cache = OrderedDict()
    lru_cache(capacity, cache, "key1", "value1")
    lru_cache(capacity, cache, "key2", "value2")
    lru_cache(capacity, cache, "key3", "value3")
    print(cache)  # Выводит OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
    lru_cache(capacity, cache, "key2", "new_value2")  # Обновлāем значение "key2"
    print(cache)  # Выводит OrderedDict([('key1', 'value1'), ('key3', 'value3'), ('key2', 'new_value2')])
    lru_cache(capacity, cache, "key4", "value4")  # Кÿш переполнен, удалāем "key1"
    print(cache)  # Выводит OrderedDict([('key3', 'value3'), ('key2', 'new_value2'), ('key4', 'value4')])


def ls28_6():
    from collections import defaultdict
    fish_inventory = [
        ("Sammy", "shark", "tank-a"),
        ("Jamie", "cuttlefish", "tank-b"),
        ("Mary", "squid", "tank-a"),
    ]


def ls28_7():
    from collections import Counter
    my_list = [1, 2, 3, 1, 2, 3, 1, 2, 4, 5, 4, 3]
    my_counter = Counter(my_list)
    print(my_counter)  # Выводит Counter({1: 3, 2: 3, 3: 3, 4: 2, 5: 1})
    print(my_counter[1])  # Выводит 3, так как ÿлемент "1" встречаетсā 3 раза в списке


def ls28_8():
    from collections import namedtuple
    Person = namedtuple("Person", ["name", "age", "city"])
    Person = namedtuple("Person", "name age city")
    person1 = Person("Alice", 30, "New York")
    person2 = Person("Bob", 25, "San Francisco")
    name, age, city = person1
    print(name, age, city)


def ls28_9():
    import json
    # Сериализациā Python-объекта в JSON-строку
    data = {"name": "John", "age": 25, "city": "New York"}
    json_str = json.dumps(data)
    print(json_str)  # Выводит '{"name": "John", "age": 25, "city": "New York"}'
    # Десериализациā JSON-строки в Python-объект
    json_str = '{"name": "John", "age": 25, "city": "New York"}'
    data = json.loads(json_str)
    print(data["name"])  # Выводит 'John'


# Дана строка.
# Посчитайте в ней частоту встречаемости всех букв.
# Считаем, что в строке могут быть
# пробельные символы.
def count_letter_frequency(s):
    from collections import Counter
    # Используем Counter для подсчета частоты каждого символа в строке
    return Counter(s)


def count_words_and_sort(text):
    from collections import Counter
    # Разбиваем текст на слова, приводим к нижнему регистру для унификации
    words = text.lower().split()

    # Подсчитываем частоту каждого слова
    word_counts = Counter(words)

    # Сортируем слова сначала по убыванию частоты, затем лексикографически
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    # Выводим отсортированный список слов
    for word, count in sorted_words:
        print(f'{word}: {count}')


if __name__ == '__main__':
    print(1, '*' * 10)
    ls28_1()
    print(2, '*' * 10)
    ls28_2()
    print(3, '*' * 10)
    ls28_3()
    print(4, '*' * 10)
    ls28_4()
    print(5, '*' * 10)
    ls28_5()
    print(8, '*' * 10)
    ls28_8()
    print(9, '*' * 10)
    ls28_9()
    print(10, '*' * 10)
    input_string = "example string with spaces"
    frequencies = count_letter_frequency(input_string)
    print(frequencies)
    print(11, '*' * 10)
    text = "Пример текста с повторяющимися словами словами словами"
    count_words_and_sort(text)
    a = {1: 2, 2: 3}
    print(a.get(1))
    print(a[1])
    print(a.get(3))
    # print[a[3]]
    from collections import defaultdict

    b = dict()
    with open('ls_26.py', 'r', encoding='utf-8') as f:
        file = f.read().split()
        print(file)
        for word in file:
            if word not in b:
                b[word] = 1
            else:
                b[word] += 1
    print(b)

    a = defaultdict(int)
    with open('ls_26.py', 'r', encoding='utf-8') as f:
        file = f.read().split()
        print(file)
        for word in file:
            a[word] += 1
    print(a)

    print('fish', '*' * 10)

    from collections import defaultdict

    fish_inventory = [
        ("Sammy", "shark", "tank-a"),
        ("Jamie", "cuttlefish", "tank-b"),
        ("Mary", "squid", "tank-a"),
    ]
    a = defaultdict(list)
    for name, species, tank in fish_inventory:
        a[tank].append((name, species))
    for key, value in a.items():
        print(key, value)

    print('Counter', '*' * 10)
    from collections import Counter

    a = defaultdict(int)
    with open('ls_26.py', 'r', encoding='utf-8') as f:
        file = f.read().split()
        print(file)
        a = Counter(file)
    print(a)

    print('Counter (file with spaces)', '*' * 10)
    with open('ls_26.py', 'r', encoding='utf-8') as file:
        file = file.read().split()
        a = Counter(file + [' '] * (len(file) - 1))
    print(a)

    from collections import namedtuple

    Person = namedtuple('Person', ['name', 'age'])
    person1 = Person('Peter', 25)
    print(person1)
    print(person1.name, person1.age)

    import json

    # Serialization
    data = {'name': 'John', 'age': 25, 'city': 'New York'}
    print(type(data), data)
    json_str = json.dumps(data)
    print(type(json_str), json_str)

    # Deserialization
    data1 = json.loads(json_str)
    print(type(data1), data1)
