name_file = input('Название файла: ')
start_file = '@№$%^&*'


for i in start_file:
    if name_file.startswith(i):
        print('Ошибка: название начинается на один из специальных символов')
        break
    # TODO, пожалуйста, обратите внимание, действия ниже, в текущем цикле, получились лишними.
    #  Условие из блока elif, необходимо проверить только один раз.
    elif not name_file.endswith('.txt' or '.docx'):  # TODO, таким образом endswith проверяет только '.txt'. Возможно, endswith стоит вызвать дважды.
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
        break
    else:
        print('Файл назван верно.')
        break
