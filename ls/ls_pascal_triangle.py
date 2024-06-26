import os


def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


def print_pascals_triangle2(triangle, output_file_path):
    max_row_length = len(" ".join(map(str, triangle[-1])))

    with open(output_file_path, 'w') as file:
        for row in triangle:
            row_str = " ".join(map(str, row))
            padding = (max_row_length - len(row_str)) // 2
            file.write(" " * padding + row_str + "\n")


def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))


def main1():
    # Считываем число n из входного файла
    file_input = os.path.join('..', 'files', 'input.txt')
    with open(file_input, 'r') as file:
        n = int(file.readline().strip())

    # Генерируем треугольник Паскаля
    triangle = generate_pascals_triangle(n)

    # Выводим треугольник Паскаля в выходной файл
    file_output = os.path.join('..', 'files', 'output.txt')
    with open(file_output, 'w') as file:
        for row in triangle:
            file.write(" ".join(map(str, row)) + "\n")


def main2():
    # Определяем путь к файлу input.txt
    input_file_path = os.path.join('..', 'files', 'input.txt')

    # Считываем число n из входного файла
    with open(input_file_path, 'r') as file:
        n = int(file.readline().strip())

    # Генерируем треугольник Паскаля
    triangle = generate_pascals_triangle(n)

    # Определяем путь к выходному файлу output.txt
    output_file_path = os.path.join('..', 'files', 'output2.txt')

    # Выводим треугольник Паскаля в выходной файл, выровненный по центру
    print_pascals_triangle2(triangle, output_file_path)


if __name__ == "__main__":
    main1()
    main2()
