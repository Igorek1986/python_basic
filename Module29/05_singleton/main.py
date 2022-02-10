from typing import Callable
import functools


def singleton(cls: Callable) -> Callable:
    """ Декоратор превращает класс в одноэлементный """

    instances = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

# 1986890616688
# 1986890616688
# True

# зачёт!

# parsing homework

# import functools
#
#
# def singleton(cls):
#     """ Декоратор класса. Превращает класс в синглтон (Может иметь только один инстанс) """
#     @functools.wraps(cls)
#     def wrapper_singleton(*args, **kwargs):
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance = cls(*args, **kwargs)
#         return wrapper_singleton.instance
#     wrapper_singleton.instance = None
#     return wrapper_singleton
#
#
# @singleton
# class Example:
#     pass
#
#
# my_obj = Example()
# my_another_obj = Example()
#
# print(id(my_obj))
# print(id(my_another_obj))
#
# print(my_obj is my_another_obj)
