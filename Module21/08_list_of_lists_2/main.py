nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def lst_open(lst):
    result = []
    for value in lst:
        if isinstance(value, list):
            result.extend(lst_open(value))
        else:
            result.append(value)
    return result


print('Ответ:', lst_open(nice_list))
