def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def inverted(hist_dict):
    lst_hist = []
    inverted_dict = dict()
    # TODO, предлагаю уйти от использования вложенных циклов, и реализовать цикле сразу по словарю hist_dict.
    #  Таким образом, мы сможем немного ускорить работу нашего кода =)
    for i_key in range(1, max(hist_dict.values()) + 1):
        for j_sym in hist:
            if hist_dict[j_sym] == i_key:
                lst_hist.append(j_sym)
        inverted_dict[i_key] = lst_hist
        lst_hist = []
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
