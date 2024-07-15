import os.path
import sys
import subprocess


def hw26_1():
    arg = sys.argv
    if len(arg) < 2:
        return 'You should setup file name for running in cmd line'
    name_file_for_run = arg[1]
    if os.path.isfile(name_file_for_run):
        if name_file_for_run.endswith('.py'):
            try:
                result_full = subprocess.run(
                    [sys.executable, name_file_for_run],
                    capture_output=True, text=True)
                result = f"File {name_file_for_run} successfully running... \n Result: {result_full.stdout}"
            except Exception as e:
                result = f'Error processing file {e}'
        else:
            ext = name_file_for_run.split('.')[1]
            result = f'Can not to run file with extension: {ext}'
    else:
        result = f'Did not find the file with name :{name_file_for_run}'
    return result


if __name__ == '__main__':
    print(hw26_1())
