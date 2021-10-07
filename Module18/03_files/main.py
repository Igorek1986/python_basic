name_file = input('Название файла: ')
start_file = '@№$%^&*'


for i in start_file:
    if name_file.startswith(i):
        print(name_file.startswith(i))
        print('Ошибка: название начинается на один из специальных символов')
        #break
    # TODO, пожалуйста, обратите внимание, действия ниже, в текущем цикле, получились лишними.
    #  Условие из блока elif, необходимо проверить только один раз.

    # if not name_file.endswith('.txt'):
    #     print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    # elif not name_file.endswith('.docx'):
    #     print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    # else:
    #     print('Файл назван верно.')

