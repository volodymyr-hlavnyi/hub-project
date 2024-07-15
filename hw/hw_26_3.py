import os
import sys


def hw26_2_2():
    arg = sys.argv
    if len(arg) == 1:
        return ['Please setup dir name in cmd line']
    start_dir = arg[1]
    return search_dir_rec(start_dir=start_dir)


def search_dir_rec(start_dir: str, dir_list: list = []):
    for file in os.listdir(start_dir):
        file_path = os.path.join(start_dir, file)
        if os.path.isdir(file_path):
            dir_list.append(file_path)
            search_dir_rec(file_path)

    return dir_list


if __name__ == '__main__':
    for name_file in hw26_2_2():
        print(name_file)
