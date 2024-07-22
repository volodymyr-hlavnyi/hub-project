import time


def ls41_1():
    def my_function_modified(func):
        def wrapper():
            print("Now run function")
            func()
            print("Function executed")

        return wrapper

    @my_function_modified
    def my_function():
        a, b = input("Введите два слова: ").split()
        print("Вот они:", b, a)

    my_function()


def ls41_2():
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Сейчас выполним функцию")

            result = func(*args, **kwargs)
            print("Функция выполнена, получено: ", result)
            return result.upper()

        return wrapper

    @decorator
    def my_function(between):
        a, b = input("Введите два слова: ").split()
        return a + between + b

    print("Результат работы декоратора: ", my_function(" and "))


def ls41_3():
    def param_decorator(ask_name):
        print(1, f'should ask a name - {ask_name}')

        def decorator(func):
            print(2, func)

            def wrapper():
                print(3, 'start wrapper func')
                if ask_name:
                    name = input("Как вас зовут? ")
                result = func()
                if ask_name:
                    print(f"Ваше имя {name}, ваш возраст - {result}")
                else:
                    print(f"Ваш возраст - {result}")
                print(5, 'done')

            return wrapper

        return decorator

    @param_decorator(False)
    def ask_age():
        print(4, 'run decorated func')
        age = input("Сколько вам лет? ")
        if age.isdigit():
            return age
        return "неизвестно"

    ask_age()


def ls41_4():
    from functools import wraps
    def log_decorator(func):
        @wraps(func)
        def wrapper():
            print(f'Вызов функции: {func.__name__}')

        func()
        return wrapper

    @log_decorator
    def hello_world():
        print("Hello, world!")

    print(hello_world.__name__)
    # Вывод: hello_world


def measure_time(point_number: int = 3):
    def decorator(func):
        def wrapper():
            start = time.time()
            # print(start)
            result = func()
            print(f"Time for execution funct {func.__name__}: {round(time.time() - start, point_number)} seconds")
            return result

        return wrapper

    return decorator


def ls41_5():
    @measure_time(3)
    def my_function():
        for _ in range(1_000_000):
            pass

    my_function()


def class_decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def __str__(self):
            return str(self.wrapped)

    return Wrapper


@class_decorator
class Person:
    def __init__(self, **kargs):
        for key, value in kargs.items():
            setattr(self, f'{key}', value)

    def __str__(self):
        text = ''
        for key, value in self.__dict__.items():
            text += f"{key}: {value}"+", "
        return "Person: " + ''.join(text[:-2])


if __name__ == '__main__':

    # ls41_1()  # my_function_modified(my_function)() -> my_function() -> my_function() -> wrapper()
    # ls41_2()  # decorator(my_function)(" and ") -> my_function(" and ") -> my_function() -> wrapper()
    # ls41_3()  # param_decorator(True)(ask_age)() -> decorator(ask_age)() -> wrapper()
    # ls41_4()  # log_decorator(hello_world)() -> hello_world() -> wrapper()
    # ls41_5()
    my_Ancle = Person(name = "Ancle", age = 25, car = "Ford")
    print(my_Ancle)
    # ls41_5()
