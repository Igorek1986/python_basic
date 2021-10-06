name_file = input('Название файла: ')
start_file = '@№$%^&*'
for i in start_file:
    if name_file.startswith(i):
        print('Ошибка: название начинается на один из специальных символов')
        break
    elif not name_file.endswith('.txt' or '.docx'):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
        break
    else:
        print('Файл назван верно.')
        break
