def long_word(lst):
    lst = max(lst, key=len)
    return lst, len(lst)


word = 'Cамоe дли слово'
word_list = word.split()
word_list = long_word(word_list)
print('Cамоe длинное слово: ', word_list[0], '-', word_list[1], 'знаков')
