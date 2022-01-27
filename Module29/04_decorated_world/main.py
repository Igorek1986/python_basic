from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator):

    def decorate():
        def info(*args, **kwargs):
            print(*args)
            return decorator(*args, **kwargs)
        return info
    return decorate


# @decorator_with_args_for_any_decorator
# def decorated_decorator(func: Callable, *args, **kwargs): # отсюда уже сами!

def decorated_decorator(func: Callable, *args, **kwargs): # отсюда уже сами!
    print('Переданные арги и кварги в декоратор:', args, kwargs)

    def wrapper():

        func(*args, **kwargs)

        @functools.wraps(func)
        def wrapped():
            func(*args, **kwargs)

        return wrapped

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


# decorated_function("Юзер", 101)


# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет Юзер 101
