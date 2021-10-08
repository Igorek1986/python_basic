def check_name(file, start_f):
    for i in start_f:
        if file.startswith(i):
            print('Ошибка: название начинается на один из специальных символов')
            return
    if file.endswith('.txt') or file.endswith('.docx'):
        print('Файл назван верно.')
    else:
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')


name_file = input('Название файла: ')
start_file = '@№$%^&*'

check_name(name_file, start_file)

# зачёт!
