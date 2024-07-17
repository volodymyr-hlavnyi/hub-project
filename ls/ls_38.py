def ls38_1():
    pass


class MyPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello {self.name} {self.age}")


class MyAnotherPerson(MyPerson):
    def __init__(self, name, age):
        super().__init__(name, age)

    def say_hello(self):
        print(f"Hallo another person {self.name} {self.age}")


class MyClass:
    class_field = "Class field"


# 1.У созданного класса Person посмотреть на уже определенные атрибуты.
# 2.Добавить какие-то поля.
# 3.Создать новый экземпляр класса.
# 4.Обратиться к именам полей через имя экземпляра класса,
# имя метода.
# 5.Рассмотреть отличия.
# 6.Попробовать изменять различными способами поля.
# 7.Удалить поля разными способами.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'


if __name__ == '__main__':
    mike = Person("Mike", 35)
    # for element in dir(mike):
    # print(f"{element} -- {mike.__getattribute__(element)}")

    # print(mike)
    # print(mike.name)
    # mike.name = 'Peter'
    # print(mike.name)

    mike.__delattr__('name')
    print(dir(mike))

    # ls38_1()
    # bob = MyPerson("Bob", 30)
    # bob.say_hello()
    #
    # tom = MyPerson("Tom", 21)
    # tom.say_hello()
    #
    # mike = MyAnotherPerson("Mike", 55)
    # mike.say_hello()
