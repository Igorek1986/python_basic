def tuple_i_i(data, sym):
    if sym in data:
        start_end = list({i for i, v in enumerate(data) if v == sym})
        if len(start_end) == 1:
            return data[start_end[0]:None]
        else:
            return data[start_end[0]:start_end[1] + 1]
    else:
        return data()


first_tuple = (1, 5, 2, 3, 1, 3, 4, 5)
elem = 1


new_tuple = tuple_i_i(first_tuple, elem)
print(new_tuple)
