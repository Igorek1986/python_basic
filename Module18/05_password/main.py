password = input('Придумайте пароль: ')
while True:
    print(not password.islower() < 1)
    print(not password.isupper() < 1)
    print(not password.isdigit() < 3)
    if not password.islower() < 1 and not password.isupper() < 1 and not password.isdigit() > 2 and len(password) > 8:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        password = input('Придумайте пароль: ')
