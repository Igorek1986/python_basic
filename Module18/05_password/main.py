def check_password(passwd):
    return not ((len(passwd) < 8) or passwd.isdigit() or passwd.isalpha() or passwd.islower() or passwd.isupper())


password = input('Придумайте пароль: ')
while True:
    if check_password(password):
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        password = input('Придумайте пароль: ')
