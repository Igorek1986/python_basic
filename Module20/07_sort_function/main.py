def sort(tuple_data):
    for i in tuple_data:
        if not isinstance(i, int):
            return tuple_data
    sorted_tuple = tuple(sorted(tuple_data))
    return sorted_tuple


original_tuple = (3, 5, 1.5, 4)
print(sort(original_tuple))
