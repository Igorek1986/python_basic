import os


def check_file(path, file, data):
    # if os.path.exists(path):
    if os.path.isfile(os.path.join(path, file)):
        while True:
            command = input('Вы действительно хотите перезаписать файл? ').lower()
            if command == 'да':
                # TODO, предлагаю написать дополнительную функцию для записи данных в файл
                #  Таким образом, получится сократить количество повторяющегося кода.
                files = open(os.path.join(path, file), 'w')
                files.write(data)
                files.close()
                print('Файл успешно перезаписан!')
                break
            elif command == 'нет':
                print('Файл не перезаписан!')
                break
            else:
                print('Проверьте команду. Введите команду "да" или "нет"')
    else:
        files = open(os.path.join(path, file), 'w')
        files.write(data)
        files.close()
        print('Файл успешно сохранён!')
    # else:
    #     print('Такой директории не существует! '
    #           'Текущий каталог', os.getcwd())


text = input('Введите строку: ')

while True:
    save = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
    cur_path = os.path.abspath(os.path.join(os.path.sep, *save))
    if os.path.exists(cur_path):
        break
    else:
        print('Такой директории не существует! '
              'Текущий каталог', os.getcwd())

name_file = input('Введите имя файла: ')
name_file = (name_file + '.txt')
check_file(cur_path, name_file, text)

if os.path.isfile(os.path.join(cur_path, name_file)):
    print('Содержимое файла: ', end='')
    dock = open(os.path.join(cur_path, name_file), 'r')
    for i_line in dock:
        print(i_line, end='')
    dock.close()

# Users igor Documents Python_Basic Module22
# my_document
