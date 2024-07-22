#
# 1. Создайте класс Rectangle для представления прямоугольника.
#
# Класс должен иметь атрибуты width (ширина) и height (высота)
# со значениями по умолчанию,
# а также методы calculate_area() для вычисления площади
# прямоугольника и calculate_perimeter() для вычисления
# периметра прямоугольника.
#
# Переопределить методы __str__, __repr__.
#
# Затем создайте экземпляр класса Rectangle
# и выведите информацию о нем, его площадь и периметр.

class Rectangle:
    def __init__(self, width: int = 1, height: int = 1):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle width={self.width}, height={self.height}"

    def __repr__(self):
        tmp = []
        tmp.append(f"Rectangle width={self.width!r}, ")
        tmp.append(f"height={self.height!r}, ")
        tmp.append(f"(calculate_area={self.calculate_area()!r}, ")
        tmp.append(f"calculate_area={self.calculate_perimeter()!r})")
        return ''.join(tmp)

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# 2. Создайте класс BankAccount для представления
# банковского счета. Класс должен иметь
# атрибуты account_number (номер счета)
# и balance (баланс),
# а также методы deposit() для внесения
# денег на счет и
# withdraw() для снятия денег со счета.
#
# Затем создайте экземпляр класса BankAccount,
# внесите на счет некоторую сумму
# и снимите часть денег.
# Выведите оставшийся баланс.
#
# Не забудьте предусмотреть вариант,
# при котором при снятии баланс может стать
# меньше нуля. В этом случае уходить в минус
# не будем, вместо чего будем возвращать
# сообщение "Недостаточно средств на счете".

class BankAccount:

    def __init__(self, account_number: str = 'DE12345', balance: int = 0, lasterror: str = ''):
        self.account_number = account_number
        self.balance = balance
        self.lasterror = lasterror

    def __str__(self):
        error_txt = f"Error: {self.lasterror}" if self.lasterror else ""
        str_text = f"Account number: {self.account_number}, balance: {self.balance}"
        if error_txt:
            str_text = f"Account number: {self.account_number}, balance: {self.balance}, {error_txt}"
        return str_text

    def __repr__(self):
        return str(self)

    def deposit(self, sum):
        self.balance += sum
        self.lasterror = ""

    def withdraw(self, sum):
        check = self.balance - sum
        if check < 0:
            self.lasterror = f"You don`t have enough money ({check}) for this operation! Cancel operation..."
        else:
            self.balance = check
            self.lasterror = ""


if __name__ == '__main__':
    rec1on1 = Rectangle()
    print(str(rec1on1))
    print(repr(rec1on1))

    my_wallet = BankAccount()
    print(my_wallet)
    my_wallet.deposit(1000)
    print(my_wallet)
    my_wallet.withdraw(999)
    print(my_wallet)
    my_wallet.deposit(2000)
    print(my_wallet)
    my_wallet.withdraw(2001)
    print(my_wallet)
    my_wallet.withdraw(2)
    print(my_wallet)
    my_wallet.deposit(100)
    print(my_wallet)
