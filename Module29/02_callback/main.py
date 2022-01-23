from typing import Callable
import functools
app = {}


def callback(key: str) -> Callable:
    def call_f(func):
        @functools.wraps(func)
        def wrapper():
            app[key] = func
        return wrapper
    return call_f


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
