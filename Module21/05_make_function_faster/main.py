def calculating_math_func(data, fact_dct={}):
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


print(calculating_math_func(10))
print(calculating_math_func(15))

# зачёт!
