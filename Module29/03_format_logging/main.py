from typing import Callable
import functools
import time
from datetime import datetime


def log_method(time_format: str, cls_name: str) -> Callable:
    """ Декоратор. Выводит имена класса, метода, время запуска и время его работы."""

    def method_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            formatted_time = ''.join('%' + alpha if alpha.isalpha() else alpha for alpha in time_format)
            print(f'- Запускается {cls_name}.{func.__name__}. '
                  f'Дата и время запуска: {datetime.now().strftime(formatted_time)}')
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'- Завершение {cls_name}.{func.__name__}, время работы = {round(end - start, 3)}s')
            return result

        return wrapped_func

    return method_decorator


def log_methods(time_format: str) -> Callable:
    """ Декоратор. Применяет декоратор log_method ко всем методам класса. """

    def wrapped(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = log_method(time_format, cls.__name__)(cur_method)
                setattr(cls, i_method_name, decorated_method)

        return cls

    return wrapped


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()


# - Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# - Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_1
# - Завершение 'A.test_sum_1', время работы = 0.187s
# Тут метод test_sum_1 у наследника
# - Завершение 'B.test_sum_1', время работы = 0.187s
# - Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_2 у наследника
# - Завершение 'B.test_sum_2', время работы = 0.370s
