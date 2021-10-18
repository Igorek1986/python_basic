def sort(tuple_data):
    flag = True
    for i in tuple_data:
        if not type(i) is int:
            flag = False
    if flag:
        sorted_tuple = sorted(tuple_data)
        return sorted_tuple
    else:
        return tuple_data


original_tuple = (3, 5, 1, 4)
print(sort(original_tuple))
