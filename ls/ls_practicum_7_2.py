import re


def task_1(s):
    # 1. Определите, содержит ли заданная строка набор данных символов (a-z, A-Z и 0-9).
    pattern = r'[a-zA-Z0-9]'
    return bool(re.search(pattern, s))


def task_2(s):
    # 2. Определите, содержит ли строка символ ‘a’, за которым следует ноль или более символов ‘b’.
    pattern = r'a[b]*'
    return bool(re.search(pattern, s))


def task_3(s):
    # 3. Определите, содержит ли строка символ ‘a’, за которым следует 1 или более символов ‘b’.
    pattern = r'a[b]+'
    return bool(re.search(pattern, s))


def task_4(s):
    # 4. Определите, содержит ли строка символ ‘a’, за которым следует 0 или 1 символ ‘b’.
    pattern = r'a[b]?'
    return bool(re.search(pattern, s))


def task_5(s):
    # 5. Определите, содержит ли строка символ z.
    pattern = r'z'
    return bool(re.search(pattern, s))


def task_6(s):
    # 6. Определите, содержит ли строка только буквы, цифры и символ подчеркивания.
    pattern = r'^\w+$'
    return bool(re.match(pattern, s))


def task_7(s, number):
    # 7. Определите, начинается ли строка с заданного числа.
    pattern = rf'^{number}'
    return bool(re.match(pattern, s))


def task_8(ip):
    # 8. Напишите программу, которая удаляет нули (0) перед цифрами в IP адресе.
    pattern = r'\b0+(\d)'
    return re.sub(pattern, r'\1', ip)


def task_9(s):
    # 9. Определите, содержит ли строка цифры в конце.
    pattern = r'\d+$'
    return bool(re.search(pattern, s))


def task_10(s, substring):
    # 10. Найдите вхождения и позиции подстроки в строке.
    matches = [(m.start(), m.end()) for m in re.finditer(re.escape(substring), s)]
    return matches


# 1. Заменяет пробелы подчеркиваниями и обратно
def replace_spaces_and_underscores(s):
    if ' ' in s:
        return s.replace(' ', '_')
    else:
        return s.replace('_', ' ')


# 12. Найти все даты в URL
def find_dates_in_url(url):
    pattern = r'/(\d{4})/(\d{2})/(\d{2})/'
    return re.findall(pattern, url)


# 13. Конвертирует дату из формата yyyy-mm-dd в формат dd-mm-yyyy
def convert_date_format(date_str):
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    match = re.match(pattern, date_str)
    if match:
        return f"{match.group(3)}-{match.group(2)}-{match.group(1)}"
    return date_str


# 14. Отделяет и печатает цифры в строке
def extract_numbers(s):
    pattern = r'\d+'
    return re.findall(pattern, s)


# 15. Выводит все слова, начинающиеся на 'a' и 'e'
def words_starting_with_ae(s):
    pattern = r'\b[aeAE]\w*'
    return re.findall(pattern, s)


# 16. Печатает цифры и их позиции в строке
def print_numbers_and_positions(s):
    pattern = r'\d'
    return [(match.group(), match.start()) for match in re.finditer(pattern, s)]


# 17. Сокращает Strasse на Str.
def replace_strasse(s):
    return s.replace('Strasse', 'Str.')


# 18. Заменяет пробелы, запятые и точки подчеркиванием
def replace_special_chars(s):
    pattern = r'[ ,.]'
    return re.sub(pattern, '_', s)


# 19. Находит все слова длины 3
def find_words_of_length_3(s):
    pattern = r'\b\w{3}\b'
    return re.findall(pattern, s)


# 20. Находит все слова длины 3, 4 и 5 символов
def find_words_of_length_3_4_5(s):
    pattern = r'\b\w{3,5}\b'
    return re.findall(pattern, s)


# 21. Превращает camel-case строку в snake-case строку
def camel_to_snake(s):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, '_', s).lower()


# 22. Выводит значения между кавычками в строке
def extract_quoted_strings(s):
    pattern = r'"(.*?)"'
    return re.findall(pattern, s)


# 23. Удаляет несколько идущих подряд пробелов из строки
def remove_multiple_spaces(s):
    pattern = r' +'
    return re.sub(pattern, ' ', s)


# 24. Удаляет все пробелы из строки
def remove_all_spaces(s):
    pattern = r' '
    return re.sub(pattern, '', s)


# 25. Заменяет все слова, начинающиеся на 'х' или 'f' на звездочки
def replace_words_with_asterisks(s):
    pattern = r'\b[xfXf]\w*'
    return re.sub(pattern, '****', s)


# Примеры использования
print(task_1("Hello123"))  # True
print(task_2("ab"))  # True
print(task_3("abbb"))  # True
print(task_4("ab"))  # True
print(task_5("pizza"))  # True
print(task_6("Hello_world123"))  # True
print(task_7("123abc", 123))  # True
print(task_8("192.01.001.10"))  # 192.1.1.10
print(task_9("abc123"))  # True
print(task_10("Домашние задания, задания в классе, отпускные задания", "задания"))

# Примеры использования:
print(replace_spaces_and_underscores("Hello World"))  # Hello_World
print(replace_spaces_and_underscores("Hello_World"))  # Hello World

url = "https://www.somesite.com/news/2024/01/22/article.html"
print(find_dates_in_url(url))  # [('2024', '01', '22')]

print(convert_date_format("2024-01-22"))  # 22-01-2024

print(extract_numbers("Ten 10, Twenty 20, Thirty 30"))  # ['10', '20', '30']

sentence = "Apple and egg are edible, and an eagle is amazing."
print(words_starting_with_ae(sentence))  # ['Apple', 'and', 'egg', 'are', 'an', 'eagle', 'is', 'amazing']

numbers_positions_str = "abc123def456"
print(print_numbers_and_positions(
    numbers_positions_str))  # [('1', 3), ('2', 4), ('3', 5), ('4', 9), ('5', 10), ('6', 11)]

print(replace_strasse("Flensburger Strasse"))  # Flensburger Str.

special_chars_str = "Hello, World. How are you?"
print(replace_special_chars(special_chars_str))  # Hello_World_How_are_you_

words_str = "This is a test string with words like cat, dog, and elephant."
print(find_words_of_length_3(words_str))  # ['cat', 'dog']

print(find_words_of_length_3_4_5(words_str))  # ['This', 'test', 'with', 'like', 'cat', 'dog', 'and']

camel_case_str = "ПайтонПрограммист"
print(camel_to_snake(camel_case_str))  # пайтон_программист

quoted_str = '"Python", "PHP", "Java"'
print(extract_quoted_strings(quoted_str))  # ['Python', 'PHP', 'Java']

multiple_spaces_str = "Hello   World   with multiple   spaces."
print(remove_multiple_spaces(multiple_spaces_str))  # Hello World with multiple spaces.

all_spaces_str = "Remove all spaces from this string."
print(remove_all_spaces(all_spaces_str))  # Removeallspacesfromthisstring.

replace_words_str = "xenon and foxes are examples of words."
print(replace_words_with_asterisks(replace_words_str))
