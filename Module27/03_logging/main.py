import functools
from typing import Callable, Any


def logging(func: Callable) -> Any:
    """ Декоратор, выполняющий функцию логирования """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Callable:
        try:
            result = func(*args, **kwargs)
            return result
        except ZeroDivisionError as error:
            with open('function_errors.log', 'a') as file:
                file.write(f'{error}\n')
            # TODO, вызывать исключения внутри этой функции не нужно, только ловить.
            raise ZeroDivisionError

    return wrapped_func


@logging
def num_zero(num):
    """ Функция для проверки деления на 0"""
    return 10 / num

# TODO, эти выводы стоит реализовать внутри декоратора.
print(num_zero.__doc__)
print(num_zero.__name__)
# print(num_zero(2))

#
for i_num in range(3):
    num_zero(i_num)


