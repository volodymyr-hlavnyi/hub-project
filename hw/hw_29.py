# 1. Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота),
# а также метод calculate_area(), который вычисляет площадь прямоугольника.
# Затем создайте экземпляр класса Rectangle с заданными значениями
# ширины и высоты и выведите его площадь.

def hw29_1():
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def calculate_area(self):
            return self.width * self.height

    my_rectangle = Rectangle(10, 10)
    print(my_rectangle.calculate_area())


# 2. Создайте класс Student для представления студента.
# Класс должен иметь атрибуты name (имя) и age (возраст),
# а также метод display_info(), который выводит информацию о студенте.
# Затем создайте экземпляр класса Student с заданным именем
# и возрастом и вызовите метод display_info().

def hw29_2():

    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def display_info(self):
            return f"This is student name: {self.name} and age: {self.age}"

    Justin = Student("Justin", 18)
    Sara = Student("Sara", 24)

    print(Justin.display_info())
    print(Sara.display_info())


if __name__ == '__main__':
    hw29_1()
    hw29_2()
