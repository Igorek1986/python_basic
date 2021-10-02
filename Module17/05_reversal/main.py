word = 'ooohokihkkk'
word_new = word[:word.index('h')] + word[word.rindex('h'):word.index('h'):-1] + word[word.rindex('h'):]


print('Слово: ', word)
print('Разворот между первой h и последней: ', word_new) #Можно не делать word_new, сразу заменить в word
