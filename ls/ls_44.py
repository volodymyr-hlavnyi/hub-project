from abc import ABC, abstractmethod


def print_name(func):
    from functools import wraps
    @wraps(func)
    def wrapper():
        print(f'{"=" * 10} {func.__name__} {"=" * 10}')
        try:
            func()
        except TypeError as e:
            print(e)

    return wrapper


@print_name
def ls44_1():
    class MyClass:
        class_atribite = "Class attribute"

        @classmethod
        def class_method(cls):
            print(cls.class_atribite)

    MyClass.class_method()


@print_name
def ls44_2():
    class Person:
        age = 25

        def printAge(cls):
            print('The age is:', cls.age)

    Person.printAge = classmethod(Person.printAge)
    Person.printAge()


@print_name
def ls44_3():
    class MyClass:
        def __init__(self):
            self._protected_attr = "Protected attribute"
            self.__private_attr = "Private attribute"

    obj = MyClass()
    print(obj._protected_attr)  # Protected attribute
    print(obj._MyClass__private_attr)  # Private attribute


@print_name
def ls44_4():
    class Shape:
        def area(self):
            raise NotImplementedError("Method 'area' must be implemented")

        def __str__(self):
            return self.__class__.__name__

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2

    class Triangle(Shape):
        def __init__(self, base, height):
            self.base = base
            self.height = height

        def area(self):
            return 0.5 * self.base * self.height

    shapes = \
        [Rectangle(5, 10),
         Circle(3),
         Triangle(10, 5)]
    for shape in shapes:
        print(shape, shape.area())


@print_name
def ls44_5():
    class A:
        def method(self):
            print("A method")

    class B(A):
        def method(self):
            print("B method")

    class C(A):
        def method(self):
            print("C method")

    class D(B, C):
        pass

    obj = D()
    obj.method()  # B method


@print_name
def ls44_6():
    class CustomException(Exception):
        pass

    try:
        raise CustomException("This is a custom exception")
    except CustomException as e:
        print(e)  # This is a custom exception


def ls44_7():
    class MyBaseClass:
        def __init__(self, x):
            self.x = x

    class MySubClass(MyBaseClass):
        def __init__(self, x, y):
            super().__init__(x)
            self.y = y

    obj = MySubClass(1, 2)
    print(obj.x)  # 1
    print(obj.y)  # 2


@print_name
def ls44_8():
    class Animal:
        def __init__(self, name):
            self.name = name

        def make_sound(self):
            print("The animal makes a sound")

    class Dog(Animal):
        def __init__(self, name):
            super().__init__(name)

        def make_sound(self):
            super().make_sound()
            print("The dog barks")

    my_dog = Dog("Buddy")
    my_dog.make_sound()


@print_name
def ls44_9():
    from abc import ABC, abstractmethod

    class AbstractClass(ABC):
        @abstractmethod
        def method(self):
            pass

    class ConcreteClass(AbstractClass):
        def method(self):
            print("ConcreteClass method")

    obj = ConcreteClass()
    obj.method()  # ConcreteClass method


@print_name
def ls44_10():
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

        @abstractmethod
        def perimeter(self):
            pass

        def __str__(self):
            return f'{self.__class__.__name__} area: {self.__class__.area()} perimeter: {self.__class__.perimeter()}'

    class Square(Shape):
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side ** 2

        def perimeter(self):
            return 4 * self.side

        def __str__(self):
            super().__str__(self)

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2

        def perimeter(self):
            return 2 * 3.14 * self.radius

        def __str__(self):
            super().__str__(self)

    square = Square(5)
    print(square)  # Square area: 25 perimeter: 20
    circle = Circle(3)
    print(circle)


@print_name
def ls44_11():
    class FirstParent:
        def some_method(self):
            print("Метод первого родителя")

    class ThirdParent(FirstParent):
        def some_method(self):
            print("Метод третьего родителя")

    class FifthChild(ThirdParent):
        def some_method(self):
            # Вызов метода первого родителя
            super(ThirdParent, self).some_method()
            print("Метод пятого наследника")

    # Создаем объект класса FifthChild
    child_obj = FifthChild()
    child_obj.some_method()


def ls44_12():
    class FirstParent:
        def some_method(self):
            self.a = 5
            print("Метод первого родителя")

    class ThirdParent(FirstParent):
        def some_method(self):
            print("Метод третьего родителя")

    class FifthChild(ThirdParent):
        def some_method(self):
            class SomeClass(ThirdParent):
                pass

            self.object1 = SomeClass()
            super(ThirdParent, self.object1).some_method()
            print("Метод пятого наследника")

    child_obj = FifthChild()
    child_obj.some_method()
    print(child_obj.object1.a)


if __name__ == '__main__':
    ls44_1()  # Class attribute
    ls44_2()
    ls44_3()
    ls44_4()
    ls44_5()
    ls44_6()
    ls44_7()
    ls44_8()
    ls44_9()
    ls44_10()
    ls44_11()
    ls44_12()
