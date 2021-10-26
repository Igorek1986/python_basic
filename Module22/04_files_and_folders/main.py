import os


# TODO, os.walk - интересное решение. Молодец! Предлагаю попробовать написать свою функцию с использованием рекурсии,
#  Вместо использования os.walk. =)


dir_path = os.path.abspath(os.path.join('..', '..', 'Module14'))
count_dir, count_file, size_file = 0, 0, 0

if os.path.exists(dir_path):
    for dir_path, dir_names, filenames in os.walk(dir_path):
        for dir_name in dir_names:
            count_dir += 1
        for filename in filenames:
            # TODO, в метод getsize() стоит передавать не только название файла но и путь от корневого диска до файла.
            #  Т.к. файлов с одинаковым названием может быть несколько. =)
            #  Иначе, рискуем получить ошибку FileNotFoundError.
            if filename != '.DS_Store':  # and filename != 'os_info.txt':
                size_file += (os.path.getsize(filename) / 1024)
                count_file += 1
else:
    print('Не верно указана директория')


print('Размер каталога (в Кб):', size_file)
print('Количество подкаталогов:', count_dir)
print('Количество файлов:', count_file)
