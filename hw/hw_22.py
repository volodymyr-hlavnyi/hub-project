# 1. Напишите программу, которая открывает файл, считывает
# из него два числа и выполняет операцию их деления.
# Если число отрицательное, выбросите исключение
# ValueError с сообщением "Число должно быть положительным".
# Обработайте исключение и выведите соответствующее сообщение.

def hw22_1():
    with open('hw_22_1.txt', 'r') as f:
        try:
            a = int(f.readline())
            b = int(f.readline())
            if a < 0 or b < 0:
                raise ValueError("Number should be positive")
            print(a / b)
        except ValueError as e:
            print(f"Error {e}")


# 2. Напишите программу, которая открывает файл, считывает его
# содержимое и выполняет операции над числами в файле.
# Обработайте возможные исключения при открытии файла
# (FileNotFoundError) и при выполнении операций
# над числами (ValueError, ZeroDivisionError).
# Используйте конструкцию try-except-finally для
# обработки исключений и закрытия файла в блоке finally.

def hw22_2():
    try:
        with open('hw_22_2.txt', 'r') as f:
            numbers = f.readlines()
    except FileNotFoundError as e:
        print("File not found")

    list = []
    for n in numbers:
        for k in n.split():
            try:
                a_int = int(k)
                list.append(a_int)
            except ValueError as e:
                print(f"Error for convert {k} in int. {e}")
    print(list)
    print(f'sum = {sum(list)}')
    for i in range(1, len(list)):
        try:
            print(f'{list[i - 1]} / {list[i]} = {list[i - 1] / list[i]}')
        except ZeroDivisionError as e:
            print(f"Error {e}")


if __name__ == '__main__':
    print('21_1', '*' * 10)
    hw22_1()

    print('22_2', '*' * 10)
    hw22_2()
