from faker import Faker


def print_name(func):
    from functools import wraps
    @wraps(func)
    def wrapper():
        print(f'{"=" * 10} {func.__name__} {"=" * 10}')
        try:
            func()
        except TypeError as e:
            print(e)

    return wrapper


@print_name
def ls45_1():
    import re
    pattern = r"\b\w{3}\b"
    text = "Hello, how are you?"
    result = re.findall(pattern, text)
    print(result)  # ['how', 'are', ‘you’]


@print_name
def ls45_2():
    import re
    pattern = r"(\b\w+)\s\1"
    text = "hello hello world world"
    result = re.findall(pattern, text)
    print(result)  # ['hello', 'world']
    replaced_text = re.sub(pattern, r"\1", text)
    print(replaced_text)  # hello world


@print_name
def ls45_3():
    import re
    text = "Python is an amazing programming language and again amazing."
    pattern = "amazing"
    match = re.search(pattern, text)
    if match:
        print("Совпадение найдено:", match.group())
    else:
        print("Совпадение не найдено")


@print_name
def ls45_4():
    import re
    text = "Hello, how are you?"
    if match := re.search(r"\b\w{3}\b", text):
        print("Match found:", match.group())
    else:
        print("No match")

    if match_all := re.findall(r"\b\w{3}\b", text):
        print("Match found:", match_all)
    else:
        print("No match")


def ls45_5():
    def func(x):
        return x

    x = 5
    result = [func(x), func(x) ** 2, func(x) ** 3]
    print(result)  # [None, None, None]
    result = [y := func(x), y ** 2, y ** 3]
    print(result)


# Написать парсер для:
# ● телефонных номеров (обработать как можно больше форматов)
# ● для email
def extract_phone_numbers(list_text):
    import re
    pattern = r"\+\d{1}\s\(\d{3,4}\)\s\d{3}-\d{2}-\d{2}"
    return_text = []
    for text in list_text:
        matches = re.findall(pattern, text)
        if len(matches) > 0:
            return_text.append(matches)  # Add all found matches to the return list

    return return_text


def extract_emails(list_text):
    import re
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return_text = []
    for text in list_text:
        matches = re.findall(pattern, text)
        if len(matches) > 0:
            return_text.append(matches)  # Add all found matches to the return list

    return return_text


if __name__ == '__main__':
    # ls45_1()  # ['how', 'are', ‘you’]
    # ls45_2()
    # ls45_3()
    # ls45_4()
    # ls45_5()
    fake = Faker()
    pattern = '+# (###) ###-##-##'
    pattern2 = '####(##)'
    list_phones = []
    list_emails = []
    for _ in range(10):
        phone_number = fake.bothify(text=pattern2)
        list_phones.append(phone_number)

    for _ in range(10):
        phone_number = fake.bothify(text=pattern)
        list_phones.append(phone_number)

    print(list_phones)
    print(extract_phone_numbers(list_phones))

    for _ in range(10):
        email = fake.email()
        list_emails.append(email)

    print(list_emails)
    print(extract_emails(list_emails))
