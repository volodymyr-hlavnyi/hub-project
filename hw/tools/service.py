from functools import wraps


def print_name(func):
    @wraps(func)
    def wrapper():
        print(f'{"=" * 10} {func.__name__} {"=" * 10}')
        func()

    return wrapper
