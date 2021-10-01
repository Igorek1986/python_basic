word = 'ooohokihkkk'
word_new = word[word.index('h') + 1:word.rindex('h')]


print('Слово: ', word)
print('Разворот между первой h и последней: ', word_new[::-1])
