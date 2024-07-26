class MyClass:
    c = 15

    def __init__(self):
        self.b = 10

    @classmethod
    def method(cls):
        cls.a = 5


print([item for item in dir(MyClass) if not item.startswith("__")])
MyClass.method()
print([item for item in dir(MyClass) if not item.startswith("__")])
my_object = MyClass()
print([item for item in dir(my_object) if not item.startswith("__")])
