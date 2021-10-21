def calculating_math_func(data, fact_dct):
    result = 1
    if data in fact_dct.keys():
        result = fact_dct[data]
    else:
        for index in range(1, data + 1):
            result *= index
            fact_dct[index] = result
    result /= data ** 3
    result = result ** 10
    return result


factorial_dct = {}
print(calculating_math_func(10, factorial_dct))
print(calculating_math_func(5, factorial_dct))
