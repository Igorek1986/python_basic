def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def inverted(hist_dict):
    inverted_dict = dict()
    for i_key in hist_dict:
        if hist_dict[i_key] in inverted_dict:
            inverted_dict[hist_dict[i_key]].append(i_key)
        else:
            inverted_dict[hist_dict[i_key]] = [i_key]
    return inverted_dict


text = input('Введите текст: ')
hist = histogram(text)


print('\nОригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])


inverted_dictionary = inverted(hist)


print('\nИнвертированный словарь частот:')
for i in range(1, len(inverted_dictionary) + 1):
    print(i, ':', inverted_dictionary[i])
