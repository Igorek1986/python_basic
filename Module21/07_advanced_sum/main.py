def lst_open(lst):
    result = []
    for value in lst:
        if isinstance(value, list):
            result.extend(lst_open(value))
        else:
            result.append(value)
    return result


print('Ответ:', lst_open([[1, 2, [3]], [1], 3]))
print('Ответ:', lst_open((1, 2, 3, 4, 5)))
# TODO, вызов функции sum получился лишним. Из нашей функции стоит возвращать сразу сумму цифр =)


# TODO, список получился лишний.
#  Предлагаю использовать переменную счётчик, они занимают на порядок меньше места в памяти, чем списки =)
