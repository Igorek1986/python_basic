from typing import Callable
import functools
app = {}


def callback(key: str) -> Callable:
    """ Декоратор. Проверяет ответ сервера. """
    def check(func):
        app[key] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return check


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')


# Ожидаемый результат:
# Пример функции, которая возвращает ответ сервера
# Ответ: OK
