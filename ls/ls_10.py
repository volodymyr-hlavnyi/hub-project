def ls10_1():
    alphabet = 'abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz'
    print(alphabet.find('bc'))
    print(alphabet.index('bc'))
    print(alphabet.find('cb'))
    # print(alphabet.index('cb'))
    new_string1 = 'Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'
    print(new_string1.find('Mars'))
    string1 = '1235896547'
    print(string1.isnumeric())
    string1 = 'asddsfkljcxmnvurtyurieвыавыавыачмчсмчс'
    print(string1.isnumeric())
    print(string1.isalpha())
    print(new_string1.islower())
    print(string1.islower())
    print(string1.isupper())
    print(new_string1.startswith('Saturn'))
    print(new_string1.endswith('Celsius.'))
    print('Mar' in new_string1)
    print('mar' in new_string1.lower())
    print(new_string1.lower())
    print(new_string1.lower().find('mar'))
    print(new_string1.upper())
    print('The Moon And The Stars'.lower())
    print('The Moon And The Stars'.upper())
    print('The Moon And The Stars'.title())
    print(new_string1.replace('a', '_'))
    print(new_string1.replace('a', '_', 3))
    template = 'The {0} brown {1} jumps over the {2} dog'
    my_template = template.format('quick', 'fox', 'lazy')
    my_template2 = template.format('lazy', 'fox', 'quick')
    print(my_template)
    print(my_template2)
    new_line = new_string1.split(' ')
    print(new_line)

    new_line2 = ' '.join(new_line)
    print(new_line2)
    a = ['Hello', '!']
    print(' '.join(a).ljust(20, '#'))
    print(' '.join(a).rjust(20, '#'))
    print(' '.join(a).center(20), '#')
    b = '--Heko--'
    print(b.lstrip('-'))
    print(b.rstrip('-'))
    print(b.strip('-'))


if __name__ == '__main__':
    ls10_1()
