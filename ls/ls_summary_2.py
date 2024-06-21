def ls1():
    n = int(input("Enter a number: "))
    n1 = 41
    while n != n1:
        print('Try again')
        n = int(input("Enter a number: "))
    else:
        print('Great! You did it!')



if __name__ == '__main__':
    ls1()
