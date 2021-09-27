guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    new_guests = input('Гость пришел или ушел? пришел\nИмя гостя: ')
    command = input('Введите команду: ')
    if len(guests) < 6 and command == 'пришел' or len(guests) < 7 and command == 'ушел':
        if command == 'пришел':
            if new_guests in guests:
                print('Человек с таким именем уже есть. Добавьте первую букву фамилии.\n')
            else:
                guests.append(new_guests)
                print('Привет, ' + str(new_guests) + '!\n')
        if command == 'ушел':
            if new_guests in guests:
                guests.remove(new_guests)
                print('Пока', new_guests)
            else:
                print('Человека с таким именем нет на вечеринке.')
    else:
        print('Прости', new_guests, 'но мест нет.\n')
