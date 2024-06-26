# 1.Веб-страницы состоят из строк типа
# "<i>Yay</i>" - выводит текст Yay курсивом. В этом
# примере, строка-тег “i” означает <i> и </i>, которые окружают слово Yay.
# Нам дана строка-тэг и текст. Написать программу, которая выводит тег вокруг
# данного текста, например,  "<i>Yay</i>". Например, ('i', 'Hello') →
# '<i>Hello</i>'.
def ls_practicum2_1_input():
    return input("Enter tag and text (|): ").split('|')


def ls_practicum2_1(tag: str = 'div', text: str = "Hello everybody") -> str:
    return f'<{tag.strip()}>{text}</{tag.strip()}>'


def ls_practicum2_1_2nput():
    return input("Enter text : ")


def ls_practicum2_2(text: str):
    return text[-2:] * 3


def ls_practicum3_1_input():
    return input("Enter string: ").lower()


def ls_practicum3_1(string1: str = 'Dog Cat cat dog'):
    return string1.count('dog') == string1.count('cat')


if __name__ == '__main__':
    # tag, text = ls_practicum2_1_input()
    print(ls_practicum2_1())
    print(ls_practicum2_2('Hello'))
    print(ls_practicum3_1())
    # string1 = input('Text for cal word: ')
    string1 = 'sdfsd sdgfsd df'
    print(string1.count(' ')+1)
    print(len(string1.split()))
    string1 = 'hello Word!'
    print(' '.join(string1.split()[::-1]))
    string1 = 'dsfdhjf kfljgkl f        f'
    # string1 = 'f dkghjdkhg'
    if string1.count('f') == 1:
        print(string1.index('f'))
    elif string1.count('f') >= 2:
        print(f"First pos: {string1.index('f')}")
        print(f"Last pos: {string1.rindex('f')}")
    else:
        print('-- not found f')

    