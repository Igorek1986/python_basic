guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    new_guests = input('Имя гостя: ')
    command = input('Гость пришел или ушел? пришел или "Пора спать!"\nВведите команду: ')
    if len(guests) < 6 and command == 'пришел' or len(guests) < 7 and command == 'ушел' or command == 'Пора спать!':
        if command == 'пришел':
            if new_guests in guests:
                print('Человек с таким именем уже есть. Добавьте первую букву фамилии.\n')
            else:
                guests.append(new_guests)
                print('Привет, ' + str(new_guests) + '!\n')
        elif command == 'ушел':
            if new_guests in guests:
                guests.remove(new_guests)
                print('Пока', new_guests, '\n')
            else:
                print('Человека с таким именем нет на вечеринке.')
        elif command == 'Пора спать!':
            print('\nСпокойной ночи!', guests)
            break
    else:
        print('Прости', new_guests, 'но мест нет.\n')

# Сейчас на вечеринке 5 человек: ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# Гость пришел или ушел? пришел
# Имя гостя: ушел
# Введите команду: Ваня
# Прости ушел но мест нет.
#  пожалуйста, обратите внимание, по идее, Ваню из списка необходимо удалить =)

# зачёт!
