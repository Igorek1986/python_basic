from typing import List


if __name__ == '__main__':
    strings: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    result = map(lambda x, y: (x, y), strings, numbers)
    print(list(result))
    # print(list(zip(strings, numbers)))

    # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
