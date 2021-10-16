count_words = int(input('Введите количество пар слов: '))
pairs_words_dict = dict()

for i_words in range(1, count_words + 1):
    pairs_words = input(f'{i_words} пара: ').split(' - ')
    pairs_words_dict[pairs_words[1]] = pairs_words[0]
    pairs_words_dict[pairs_words[0]] = pairs_words[1]

while True:
    word = input('Введите слово: ').title()
    if word in pairs_words_dict:
        print(f'Синоним: {pairs_words_dict[word]}')
        break
    else:
        print('Такого слова в словаре нет.')

# зачёт!
