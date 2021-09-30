# word = 'dfergHewrterglHeteteHt'
word = 'ooohokihkkk'

# TODO, пожалуйста, обратите внимание, циклы в данном задании не нужны,
#  предлагаю попробовать решить только при помощи поиска элементов по индексу и срезам.
#  Ознакомиться с методами index и rindex, и их параметрами можно:
#  https://pythonz.net/references/named/str.rindex/
#  https://pythonz.net/references/named/str.index/


word_new = [word[i+1:] for i in range(len(word)) if word[i] == 'H']
word_new = word_new[0]
word_new = [word[:i+1] for i in range(len(word_new), 0, -1) if word[i] == 'H']
word_new = word_new[0]



print('Слово: ', word)
print('Разворот между первой h и последней: ', word_new[::-1])