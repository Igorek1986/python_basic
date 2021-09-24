films_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_list = []

films = input('Название фильма: ')
while films != 'end':
    for index in range(len(films_list)):
        if films_list[index] == films:
            favorite_list.append(films_list[index])
    films = input('Название фильма: ')
print(favorite_list)

