class Cat:
    animal = 'Cat'

    def __init__(self, name: str = 'saturn', age: int = 1):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def __repr__(self):
        return f"Cat(name='{self.name}!r' age='{self.age}!r)'"

    @staticmethod
    def my_print(str4print):
        Utils.print_my(str4print)


class Utils:
    @staticmethod
    def print_my(str4print):
        print(str4print)


#
# my_cat = Cat()
# print(my_cat)
# print(my_cat.my_print('cat saturn'))
# print(repr(my_cat))


# Cоздать класс окружности, определить методы для площади и длины окружности
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle R={self.radius}"

    def __repr__(self):
        return f"Circle R={self.radius}"

    def calc_square(self):
        return 3.14 * self.radius ** 2

    def calc_lenght(self):
        return 2 * 3.14 * self.radius


from random import randint

list_my_circle_1 = [Circle(randint(1, 11)) for x in range(10)]
print(list_my_circle_1)
max_circle = max(list_my_circle_1, key=lambda c: c.radius)
print(list_my_circle_1.index(max_circle))