# 1. Напишите программу, которая
# запрашивает у пользователя целое число и
# определяет, является ли оно палиндромом.
# Число является палиндромом, если оно
# читается одинаково слева направо и
# справа налево.
# Выведите соответствующее сообщение на
# экран с помощью команды print.
# Используйте математические операции.
# Работу со строками использовать нельзя.
#
#
# Пример вывода:
#
# Введите целое число: 12321
#
# Число является палиндромом.
#
def hw8_1(enter_number: int):
    temp = enter_number
    reverse = 0
    while enter_number > 0:
        digit = enter_number % 10
        reverse = reverse * 10 + digit
        enter_number = enter_number // 10
    if temp == reverse:
        return "The number is a palindrome."
    else:
        return "The number isn't a palindrome."


# 2. Напишите программу, которая запрашивает
# у пользователя целое число и проверяет,
# является ли оно числом Армстронга.
# Число Армстронга - это число, которое
# равно сумме своих цифр, возведенных в степень,
# равную количеству цифр в числе.
# Выведите соответствующее сообщение
# на экран с помощью команды print.
#
#
# Пример вывода:
#
# Введите целое число: 153
#
# Число является числом Армстронга.
def hw8_2(enter_number: int):
    temp = enter_number
    sum = 0
    n = len(str(enter_number))
    while enter_number > 0:
        digit = enter_number % 10
        sum += digit ** n
        enter_number = enter_number // 10
    if temp == sum:
        return "The number is an Armstrong number."
    else:
        return "The number isn't an Armstrong number."


if __name__ == '__main__':
    number = int(input("Enter a number (for check is palindrome): "))
    print(hw8_1(number))
    numer = int(input("Enter a number (for check is numberArmstrong): "))
    print(hw8_2(numer))
