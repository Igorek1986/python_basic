import time
import functools
from typing import Callable, Any


def sleap(func: Callable, timeout=3) -> Callable:

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(f'Сон на {timeout} секунд')
        time.sleep(timeout)
        print("Как дела? Хорошо.\n"
              "А у меня не очень! Ладно, держи свою функцию.")
        result = func(*args, **kwargs)

        return result
    return wrapped_func


@sleap
def test():

    print('<Тут что-то происходит...>')


test()
