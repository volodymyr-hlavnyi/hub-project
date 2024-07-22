# Python: домашние задание 32 morning (Python)
#
# 1. Реализовать класс Counter, который представляет счетчик.
# Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)

from functools import wraps


def print_name_func(func):
    @wraps(func)
    def wrapper():
        print(f'{"=" * 5} {func.__name__} {"=" * 5}')
        func()

    return wrapper


class Counter:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Counter(self.count + other)

    def __sub__(self, other):
        return Counter(self.count - other)

    def __str__(self):
        return f'{self.count}'

    def __int__(self):
        return self.count


@print_name_func
def hw32_1():
    counter = Counter(5)
    print(counter)  # Вывод: 5
    counter += 3
    print(counter)  # Вывод: 8
    counter -= 2
    print(counter)  # Вывод: 6


# 2. Реализовать класс Email, представляющий электронное письмо.
# Класс должен поддерживать следующие операции:
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)

class Email:
    def __init__(self, from_email, to_email, subject, text, date):
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject
        self.text = text
        self.date = date

    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date

    def __le__(self, other):
        return self.date <= other.date

    def __ge__(self, other):
        return self.date >= other.date

    def __eq__(self, other):
        return self.date == other.date

    def __ne__(self, other):
        return self.date != other.date

    def __str__(self):
        list_email = []
        list_email.append(f'From: {self.from_email}')
        list_email.append(f'To: {self.to_email}')
        list_email.append(f'Subject: {self.subject}')
        list_email.append(self.text)
        return '\n'.join(list_email)

    def __len__(self):
        return len(self.text)

    def __hash__(self):
        return hash(self.text)

    def __bool__(self):
        return bool(self.text)


@print_name_func
def hw32_2():
    email1 = Email("john@example.com", "jane@example.com", "Meeting",
                   "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")
    email2 = Email("jane@example.com", "john@example.com", "Re: Meeting",
                   "Sure, let's meet at 2 PM.", "2022-05-10")
    email3 = Email("alice@example.com", "bob@example.com", "Hello",
                   "Hi Bob, how are you?", "2022-05-09")
    print(email1)
    print(f'len(email2): {len(email2)}')  # Вывод: 24
    print(hash(email3))  # Вывод: -920444056
    print(bool(email1))  # Вывод: True
    print(email2 > email3)  # Вывод: True


if __name__ == '__main__':
    hw32_1()
    hw32_2()
