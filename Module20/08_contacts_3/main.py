def add_book(p_dict, string):
    surname_name = tuple(string[:2])
    tel = string[2]
    if surname_name in p_dict:
        print('Такая фамилия и имя уже есть в БД. Запись не произведена!')
    else:
        p_dict[surname_name] = tel
        for i_person, i_tel in p_dict.items():
            print(f'{i_person[0]} {i_person[1]}: {i_tel}')


def search_people(surname):
    if surname[-1] == 'а':
        surname = surname[:-1]
    for people, age in phonebook.items():
        if surname in people[0]:
            print(people[0], people[1], age)


phonebook = {}

while True:
    action = input('\n"добавить контакт" или "найти человека", '
                   '"стоп" для выхода: ').lower()
    if action == 'добавить контакт':
        person = input('Введите Фамилию Имя и телефон через пробел: ').title().split()
        print('')
        add_book(phonebook, person)
    elif action == 'найти человека':
        surname_search = input('Введите фамилию для поиска: ').title()
        search_people(surname_search)
    elif action == 'стоп':
        print('До свидания!')
        break
    else:
        print('Ошибка ввода команды!')

# зачёт!
