import sys
import argparse
import os


def ls_34_1():
    args = sys.argv
    print(args)


def ls_34_2():
    args = sys.argv
    print(sys.argv)
    print([arg for arg in sys.argv if arg[0] != '-'])


def ls_34_3():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to input file')
    parser.add_argument('-o', '--output', help='Path to output file')
    args = parser.parse_args()
    count_lines(args.input)
    print(args.input)
    print(count_lines(args.input))


def clear_word(word: str):
    word = word.lower()
    return ''.join([symbol for symbol in word if symbol.isalpha()])

    with open(args.input, 'r', encoding='utf-8') as input_file:
        input_file = list(map(clear_word, input_file.read().split()))

    with open(args.output, 'w', encoding='utf-8') as output_file:
        for word in input_file:
            output_file.write(f'{word}\n')


def count_lines(file):
    with open(file, 'r') as f:
        return len(f.readlines())


def ls_34_4():
    os.chdir('.')
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    # os.mkdir('new_directory')
    # os.makedirs('new_directory/sub_directory')
    for dirpath, dirnames, filenames in os.walk(current_dir):
        for filename in filenames:
            if '.py' in filename:
                print(os.path.join(dirpath, filename))


def ls_34_5():
    path = os.path.join('/ls/to', 'file.txt')
    absolute_path = os.path.abspath(path)
    exists = os.path.exists(absolute_path)
    is_directory = os.path.isdir(absolute_path)
    is_file = os.path.isfile(absolute_path)


def ls_34_6():
    def process_directory(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if all(map(lambda x: x not in file_path, ['.venv', '.git', '.idea', '.py'])):
                if os.path.isfile(file_path):
                    # Обработка файла
                    print(file_path)
                elif os.path.isdir(file_path):
                    # Рекурсивный вызов для вложенного каталога
                    process_directory(file_path)

    start_directory = '/home/vladimir/develop/python'
    process_directory(start_directory)


def ls34_7(directory):
    def process_directory(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            # if all(map(lambda x: x in file_path, ['.txt'])):
            # if '.txt' in file_path:
            if file_path.endswith('.txt'):
                if os.path.isfile(file_path):
                    # Обработка файла
                    print(file_path)
                elif os.path.isdir(file_path):
                    # Рекурсивный вызов для вложенного каталога
                    process_directory(file_path)

    process_directory(directory)


if '__main__' == __name__:
    # ls_34_1()

    # ls_34_2()
    # ls_34_3()
    # ls_34_4()
    # ls_34_6()
    ls34_7('.')
