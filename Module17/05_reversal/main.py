word = 'dfergHewrterglHeteteHt'


word_new = [word[i+1:] for i in range(len(word)) if word[i] == 'H']
word_new = word_new[0]
word_new = [word[:i+1] for i in range(len(word_new), 0, -1) if word[i] == 'H']
word_new = word_new[0]



print('Слово: ', word)
print('Разворот между первой h и последней: ', word_new[::-1])