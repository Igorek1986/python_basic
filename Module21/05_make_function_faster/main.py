def calculating_math_func(data, fact_dct):
    result = 1
    if not fact_dct:
        start = 0
    else:
        start = list(fact_dct.keys())[-1]
    if data in fact_dct.keys():
        result = fact_dct[data]
    else:
        for index in range(start + 1, data + 1):
            result *= index
            fact_dct[index] = result
    result /= data ** 3
    result = result ** 10
    return result


factorial_dct = {}
# TODO, предлагаю просто перенести эту строку в параметры нашей функции.
#  Иначе, при повторном запуске функции словарь пересоздаётся и изменения,
#  которые мы произвели в нём при первом запуске функции не сохраняются.
#  Но, если реализовать пустой словарь как параметр по умолчанию, при повторном запуске функции
#  мы можем обратиться к его элементам.
#  Ничего страшного, если PyCharm будет ругаться. Таким образом, мы создаём буфер памяти только для нашей функции.



print(calculating_math_func(10, factorial_dct))
print(calculating_math_func(15, factorial_dct))
