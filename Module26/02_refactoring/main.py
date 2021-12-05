from collections.abc import Iterable


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def find_num() -> Iterable[int]:
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result)
            if result == to_find:
                print('Found!!!')
                yield result
                return result


for i_value in find_num():
    print(i_value)
