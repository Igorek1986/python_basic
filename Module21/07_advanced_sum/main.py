def lst_open(lst):
    result = []
    for value in lst:
        if isinstance(value, list):
            result.extend(lst_open(value))
        else:
            result.append(value)
    return result


print('Ответ:', sum(lst_open([[1, 2, [3]], [1], 3])))
print('Ответ:', sum(lst_open((1, 2, 3, 4, 5))))
