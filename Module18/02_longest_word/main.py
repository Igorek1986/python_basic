word = 'Cамоe дли слово'
word_list = word.split()
print('Cамоe длинное слово: ', max(word_list, key=len), '-', len(max(word_list, key=len)), 'знаков')
