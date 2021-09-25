films_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_list = []


films = input('Название фильма: ')
while films != 'end':
    for index in films_list:
        if index == films:
            favorite_list.append(index)
            break
    films = input('Название фильма: ')


print(favorite_list)
