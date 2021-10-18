def tuple_i_i(data, sym):
    if sym in data:
        start = data.index(sym)
        if data.count(sym) > 1:
            end = data.index(sym, start + 1)
            return data[start:end + 1]
        else:
            return data[start:]
    else:
        return data[0:0]


first_tuple = (1, 5, 2, 3, 1, 3, 4, 5)
elem = 6


new_tuple = tuple_i_i(first_tuple, elem)
print(new_tuple)
