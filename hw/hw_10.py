# 1. Напишите программу, которая
# запрашивает у пользователя строку
# и преобразует ее, удаляя все гласные
# буквы из строки. Используйте метод replace()
# для замены гласных букв на пустую строку.
# Выведите преобразованную строку на экран с
# помощью команды print.
#
#
# Пример вывода:
# #
# Введите строку: Hello, world!
#
# # Результат: Hll, wrld!
def hw10_1(input_string: str = 'Hello, world!'):
    vowels = 'aeiou'
    for i in vowels:
        input_string = input_string.replace(i, '')
    return input_string

    # 2. Напишите программу, которая запрашивает
    # у пользователя строку и определяет, содержит
    # ли она только уникальные символы.
    # Если все символы в строке уникальны, выведите
    # соответствующее сообщение на экран.
    # В противном случае выведите сообщение о том,
    # какие символы повторяются. Не используйте
    # множества и подобные структуры данных,
    # которые мы пока не изучали, для проверки
    # уникальности символов.
    #
    #
    # Пример вывода:
    # #
    # Введите строку: Python
    # #
    # Все символы в строке уникальны.
    # #
    # Введите строку: Hello World!
    #
    # # Символы 'l' и 'o' повторяются.


def hw10_2(input_string: str = 'Hello'):
    str_what_repeated = ''
    for i in input_string:
        if input_string.count(i) > 1:
            if i not in str_what_repeated:
                str_what_repeated += i
    if str_what_repeated not in '':
        str_4_print = f"{' and '.join(str_what_repeated)}"
        return f"Symbols {str_4_print} repeat."
    else:
        return "All symbols in the string are unique."


# 3. Напишите программу, которая запрашивает у
# пользователя строку и выравнивает ее по центру
# с заданной шириной. Если строка не может быть
# выровнена по центру из-за нечетной ширины,
# она должна быть выровнена смещением вправо.
# Используйте методы center() и rjust() для
# выравнивания строки.
#
#
# Пример вывода:
#
# Введите строку: Python
# Введите ширину: 10
#
# Результат:
#   Python
def hw10_3(input_string: str = 'Python', width: int = 10):
    if width % 2 == 0:
        return input_string.center(width)
    else:
        return input_string.rjust(width)


if __name__ == '__main__':
    print(hw10_1())
    inp_str = input('Enter a string (default Hello World!): ')
    if inp_str == '':
        inp_str = 'Hello World!'
    print(hw10_2(inp_str))
    inp_str = input('Enter a string (default Python): ')
    inp_width = input('Enter a width (default 10): ')
    if inp_str == '':
        inp_str = 'Python'
    if inp_width == '':
        inp_width = 10
    print(hw10_3(inp_str, inp_width))
