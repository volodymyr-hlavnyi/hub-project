# Erstellen Sie einen Generator,
# der eine Liste von Zahlen akzeptiert
# und Zeichenfolgen zurückgibt,
# die aus diesen Zahlen bestehen
# und rechts auf eine Länge von 10 Zeichen
# mit Nullen aufgefüllt werden.

def fillWithZeros(lst):
    for i in lst:
        yield str(i).rjust(10, '0')



if __name__ == '__main__':
    lst = [1, 10, 100, 1000, 10000]
    print('before:')
    for i in lst:
        print(i)
    print('after:')
    for i in fillWithZeros(lst):
        print(i)
