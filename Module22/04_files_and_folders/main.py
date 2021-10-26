import os


dir_path = os.path.abspath(os.path.join('..', '..', 'Module14'))
count_dir, count_file, size_file = 0, 0, 0

if os.path.exists(dir_path):
    for dir_path, dir_names, filenames in os.walk(dir_path):
        for dir_name in dir_names:
            count_dir += 1
        for filename in filenames:
            if filename != '.DS_Store':  # and filename != 'os_info.txt':
                size_file += (os.path.getsize(filename) / 1024)
                count_file += 1
else:
    print('Не верно указана директория')


print('Размер каталога (в Кб):', size_file)
print('Количество подкаталогов:', count_dir)
print('Количество файлов:', count_file)
