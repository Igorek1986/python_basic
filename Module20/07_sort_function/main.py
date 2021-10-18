def sort(tuple_data):
    # TODO, переменная флаг получилась лишней.
    flag = True
    for i in tuple_data:
        # TODO Для проверки типа числа стоит использовать функцию isinstance.
        if not type(i) is int:
            flag = False
            # TODO, если хотя бы одно число не целое, стоит сразу вернуть неотсортированный кортеж.
    # TODO, если внутри цикла кортеж не вернули, сразу после него стоит вернуть отсортированный кортеж =)
    if flag:
        sorted_tuple = sorted(tuple_data)  # TODO функция sorted возвращает список, стоит привести его к кортежу. =)
        return sorted_tuple
    else:
        return tuple_data


original_tuple = (3, 5, 1, 4)
print(sort(original_tuple))
