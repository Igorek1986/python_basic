import functools
import random
from typing import Callable, Any


def logging(func: Callable) -> Any:
    """ Декоратор, выполняющий функцию логирования """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Callable:
        print(func.__doc__)
        print(func.__name__)
        try:
            result = func(*args, **kwargs)
            return result
        except ZeroDivisionError as error:
            with open('function_errors.log', 'a') as file:
                file.write(f'{error}\n')

    return wrapped_func


@logging
def num_zero(num: int) -> float:
    """ Функция для проверки деления на 0 """
    return 10 / num


for _ in range(10):
    num_zero(num=random.randint(0, 1))

# зачёт!
