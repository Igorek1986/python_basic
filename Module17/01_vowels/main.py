word = 'Нужно отнести кольцо в Мордор!'  # input('Введите текст: ')

word_new = [x for x in word for y in ('ауоыэяюёие') if x == y]

print(word_new)
print('Длина списка:', len(word_new))

# зачёт!
