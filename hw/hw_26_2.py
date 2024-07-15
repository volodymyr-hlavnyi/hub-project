import os
import sys


def search_dir(start_dir):
    dir_list = []
    for dirpath, dirnames, filenames in os.walk(start_dir):
        for filename in filenames:
            dir_list.append(os.path.join(dirpath, filename))
    return dir_list


def hw26_2_1():
    arg = sys.argv
    if len(arg) == 1:
        return ['Please setup dir name in cmd line']
    start_dir = arg[1]
    # start_dir = "/home/vladimir/develop/python/ich-hub"
    return search_dir(start_dir)


if __name__ == '__main__':
    for name_file in hw26_2_1():
        print(name_file)
