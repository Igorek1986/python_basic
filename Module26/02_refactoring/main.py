from collections.abc import Iterable


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def find_num(lst1: list, lst2: list, find_num: int) -> Iterable[int]:
    for x in lst1:
        for y in lst2:
            result = x * y
            yield x, y, result
            if result == find_num:
                print('Found!!!')
                yield result
                return result


for i_value in find_num(lst1=list_1, lst2=list_2, find_num=to_find):
    print(i_value)
