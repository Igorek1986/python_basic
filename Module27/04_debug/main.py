import functools
from typing import Callable


def debug(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs) -> str:

        info = str(func.__name__)
        info += "("

        if args:
            info += ''.join("'" + x + "'" for x in args)

        if kwargs:
            info += ', '.join(x + '=' + "'" + str(y) + "'" for x, y in kwargs.items())

        else:
            info += ''.join('')

        info += ")"

        print('Вызывается', info)
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' вернула значение '{result}'")
        return result

    return wrapper_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting("Том"), '\n')
print(greeting(name="Миша", age=100), '\n')
print(greeting(name="Катя", age=16), '\n')

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

# зачёт!
