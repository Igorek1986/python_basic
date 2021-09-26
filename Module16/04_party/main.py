def is_guests_exist(guest, guests_list):
    for i_guest in guests_list:
        if i_guest != guest:
            return True
    return False


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    new_guests = input('Гость пришел или ушел? пришел\nИмя гостя: ')
    if len(guests) <=6:
        if is_guests_exist(new_guests, guests):
            command = input('Введите команду: ')
            if command == 'пришел':
                if is_guests_exist(new_guests, guests):
                    print('Человек с таким именем уже есть. Добавьте первую букву фамилии.\n')
                else:
                    guests.append(new_guests)
                    print('Привет, ' + str(new_guests) + '!\n')
            if command == 'ушел':
                if is_guests_exist(new_guests, guests):
                    print('Человека с таким именем нет на вечеринке.')
                else:
                    guests.remove(new_guests)
                    print('Пока', new_guests)
    else:
        print('Прости', new_guests, 'но мест нет.\n')
