# 1. Реализуйте класс Employee,
# представляющий сотрудника компании.
# Класс должен иметь статическое поле company
# с названием компании,
# а также методы:
# set_company(cls, name):
# метод класса для изменения названия компании
# __init__(self, name, position):
# конструктор, принимающий имя и должность сотрудника
# get_info(self):
# метод, возвращающий информацию о сотруднике
# в виде строки (имя, должность, название компании)
#
# Пример использования:
#
# employee1 = Employee("John", "Manager")
# employee2 = Employee("Alice", "Developer")
# print(employee1.get_info())  # Вывод:
#
# """
# Name: John
# Position: Manager
# Company: ABC Company
# """
#
# Employee.set_company("XYZ Company")
# print(employee2.get_info())  # Вывод:
#
# """
# Name: Alice
# Position: Developer
# Company: XYZ Company
# """
from math import sqrt, pi
from abc import abstractmethod

from tools.service import print_name


@print_name
def hw33_1():
    class Employee:
        company = "ABC Company"

        @classmethod
        def set_company(cls, name):
            cls.company = name

        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_info(self):
            return f'Name: {self.name}\nPosition: {self.position}\nCompany: {self.company}'

    employee1 = Employee("John", "Manager")
    employee2 = Employee("Alice", "Developer")
    print(employee1.get_info())
    print('---')
    Employee.set_company("XYZ Company")
    print(employee2.get_info())


@print_name
def hw33_2():
    class Shape:
        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            pass

        def __str__(self):
            return f'{self.__class__.__name__} area: {self.__class__.area()} perimeter: {self.__class__.perimeter()}'

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return self.radius * sqrt(pi)

        def perimeter(self):
            return self.radius * 2 * pi

    class Rectangle(Shape):
        def __init__(self, width, hight):
            self.width = width
            self.hight = hight

        def area(self):
            return self.width * self.hight

        def perimeter(self):
            return 2 * (self.width + self.hight)

    rectangle = Rectangle(5, 3)
    circle = Circle(2)

    print(f"Rectangle area: {rectangle.area()}")  # Вывод: Rectangle area: 15
    print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Вывод: Rectangle perimeter: 16
    print(f"Circle area: {circle.area()}")  # Вывод: Circle area: 12.566370614359172
    print(f"Circle perimeter: {circle.perimeter()}")


if __name__ == '__main__':
    hw33_1()
    hw33_2()
