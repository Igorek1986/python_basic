from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """ Декоратор принимающий декоратор.
    С произвольным кол-вом аргументов """

    def decorator_maker(*args, **kwargs):
        @functools.wraps(decorator)
        def decorator_wrapper(func):
            return decorator(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    """ Декоратор декорируемый другим декоратором """

    @functools.wraps(func)
    def wrapper(func_arg1, func_arg2):
        print('Переданные арги и кварги в декоратор:', args, kwargs)
        return func(func_arg1, func_arg2)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет Юзер 101

# зачёт!
