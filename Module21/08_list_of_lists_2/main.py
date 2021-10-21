nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


# def lst_open(lst):
#     result = []
#     for value in lst:
#         if isinstance(value, list):
#             result.extend(lst_open(value))
#         else:
#             result.append(value)
#     return result
def lst_open(lst):
    if not lst:
        return lst
    if isinstance(lst[0], list):
        return lst_open(lst[0]) + lst_open(lst[1:])
    else:
        return lst[:1] + lst_open(lst[1:])


print('Ответ:', lst_open(nice_list))
