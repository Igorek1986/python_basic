while True:
    user_name = input('Введите имя пользователя: ')
    action = input('Введите действие\n'
                   '1 - Просмотреть чат:\n'
                   '2 - Отправить сообщение:\n'
                   '3 - Выход из чата.\n'
                   'Введите действие: ')
    try:
        if not 'chat.txt':
            raise FileNotFoundError
        if action == '1':
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                print(*chat)
        elif action == '2':
            with open('chat.txt', 'a+', encoding='utf-8') as chat:
                chat.seek(0)
                for line in chat.readlines():
                    print(line, end='')
                message = input('Введите сообщение: ')
                chat.write(f'{user_name}: {message}\n')
        elif action == '3':
            print('Выход из чата!')
            break
        else:
            print('Некорректный выбор действия\n'
                  'введите 1, 2 или 3')
    except FileNotFoundError:
        print('Файл не создан! Чат пустой')
