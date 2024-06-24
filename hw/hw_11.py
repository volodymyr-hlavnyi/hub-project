# 1. Напишите программу, которая запрашивает у
# пользователя его имя, возраст и место проживания,
# а затем выводит их в следующем формате:
#
# "Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}."
#
#
# Вместо {0}, {1} и {2} подставьте соответствующие значения.
# Используйте метод format() для форматирования строки.
# Потом попробуйте использовать f-строку.
# Выведите результат на экран с помощью команды print.
#
#
# Пример вывода:
#
#
# Введите ваше имя: Alice
#
# Введите ваш возраст: 25
#
# Введите ваше место проживания: London
#
#
# Привет, меня зовут Alice. Мне 25 лет. Я живу в London.

def hw11_1_input():
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    city = input('Enter your city: ')
    return name, age, city


def hw11_1_1(name, age, city):
    return 'Hello, my name is {}. I am {} years old. I live in {}.'.format(name, age, city)


def hw11_1_2(name, age, city):
    return f'Hello, my name is {name}. I am {age} years old. I live in {city}.'


# 2. Напишите программу, которая запрашивает у пользователя
# два числа и выводит их сумму и произведение
# в следующем формате:
#
# "Сумма: {sum:.2f}, Произведение: {product:.2f}"
#
# Вместо {sum:.2f} и {product:.2f} подставьте соответствующие значения, округленные до двух десятичных знаков. Используйте f-строки с использованием форматных спецификаторов для форматирования чисел. Выведите результат на экран с помощью команды print.
#
# Пример вывода:
#
# Введите первое число: 3.14159
# Введите второе число: 2.71828
#
# Сумма: 5.86, Произведение: 8.54
def hw11_2_input():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    return num1, num2


def hw11_2(num1, num2):
    return f'Sum: {num1 + num2:.2f}, Product: {num1 * num2:.2f}'


if __name__ == '__main__':
    name, age, city = hw11_1_input()
    print(hw11_1_1(name, age, city))
    print(hw11_1_2(name, age, city))
    num1, num2 = hw11_2_input()
    print(hw11_2(num1, num2))
