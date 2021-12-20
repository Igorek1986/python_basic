import functools
from typing import Callable, Any


def debug(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs) -> Any:

        info = str(func.__name__)
        info += "('"

        if args:
            for i_args in args:
                info += ''.join(i_args)

        else:
            for i_key, i_value in kwargs.items():
                # info += str(i_key) + '=' + str(i_value)
                info += ''.join(i_key) + '=' + str(i_value)
        info += "')"
        print('Вызывается', info)
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' вернула значение {result}")
        return print(result)

    return wrapper_func


@debug
def greeting(name, age=None):

    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
print()
greeting(name="Миша", age=100)
print()
greeting(name="Катя", age=16)


# Результат:

# Вызывается greeting('Том')
# 'greeting' вернула значение 'Привет, Том!'
# Привет, Том!


# Вызывается greeting('Миша', age=100)
# 'greeting' вернула значение 'Ого, Миша! Тебе уже 100 лет, ты быстро растёшь!'
# Ого, Миша! Тебе уже 100 лет, ты быстро растешь!


# Вызывается greeting(name='Катя', age=16)
# 'greeting' вернула значение 'Ого, Катя! Тебе уже 16 лет, ты быстро растёшь!'
# Ого, Катя! Тебе уже 16 лет, ты быстро растешь!
