import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        input("Какой у тебя вопрос? \n")
        print("Хорошо.\n"
              "А у меня не очень! Ладно, держи свою функцию.")
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()

# Результат:
# Как дела? Хорошо.
# А у меня не очень! Ладно, держи свою функцию.
# <Тут что-то происходит...>

# зачёт!
