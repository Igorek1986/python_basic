from collections.abc import Iterable


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
# TODO, все переменные стоит передавать в функцию как параметры.
#  Если переменные созданы не будут, то при вызове функции мы можем получить ошибку.

# TODO, пожалуйста, не забудьте добавить аннотации к параметрам функции.
def find_num() -> Iterable[int]:
    for x in list_1:
        for y in list_2:
            result = x * y
            # TODO, текст, который сейчас выводится при помощи print, стоит возвращать из итератора при помощи yield.
            print(x, y, result)
            if result == to_find:
                print('Found!!!')
                yield result
                return result


for i_value in find_num():
    print(i_value)
