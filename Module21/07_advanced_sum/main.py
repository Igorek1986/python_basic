# def lst_open(lst):
#     result = []
#     for value in lst:
#         if isinstance(value, list):
#             result.extend(lst_open(value))
#         else:
#             result.append(value)
#     return result


def lst_open(lst):
    lst_sum = 0
    count = len(lst)
    if count == 0:
        return 1
    for value in lst:
        if isinstance(value, list):
            lst_sum += lst_open(value)
        else:
            count -= 1
            lst_sum += value
    return lst_sum


print('Ответ:', lst_open([[1, 2, [3]], [1], 3]))
print('Ответ:', lst_open((1, 2, 3, 4, 5)))

# зачёт!
