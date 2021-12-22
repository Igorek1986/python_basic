from typing import Callable


class Counter:

    """ Подсчет количества вызова декорируемой функции """

    count = 0

    def __init__(self, func: Callable) -> None:
        self.func = func

    def __call__(self, *args, **kwargs) -> int:
        self.count += 1
        return self.count


@Counter
def hallo_word():
    print('hallo_word')


hallo_word()
hallo_word()
print('Функция вызывалась:', hallo_word.count, 'раза!')
