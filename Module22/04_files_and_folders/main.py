import os


def os_walk(cur_path, size_dirs, sub_dirs_count, files_count):
    if os.path.exists(cur_path):
        for cur_path, dir_names, filenames in os.walk(cur_path):
            for dir_name in dir_names:
                sub_dirs_count += 1
            for filename in filenames:
                if filename != '.DS_Store':  # and filename != 'os_info.txt':
                    size_dirs += (os.path.getsize(os.path.join(cur_path, filename)) / 1024)
                    files_count += 1
    else:
        print('Не верно указана директория')
    return size_dirs, sub_dirs_count, files_count


def dir_files(cur_path, size_dirs, sub_dirs_count, files_count):
    if os.path.exists(cur_path):
        for i_elem in os.listdir(cur_path):
            path = os.path.join(cur_path, i_elem)
            sub_dirs_count += 1
            if os.path.isfile(path) and i_elem != '.DS_Store':
                files_count += 1
                size_dirs += os.path.getsize(os.path.join(cur_path, i_elem)) / 1024
            if os.path.isdir(path):
                dir_files(path, size_dirs, sub_dirs_count, files_count)





        return size_dirs, sub_dirs_count, files_count
        # print('Кол-во папок', sub_dirs_count)
        # print('Кол-во файлов', files_count)
    else:
        print('Не верно указана директория')


# TODO, os.walk - интересное решение. Молодец! Предлагаю попробовать написать свою функцию с использованием рекурсии,
#  Вместо использования os.walk. =)


dir_path = os.path.abspath(os.path.join('..', '..', 'Module14'))
count_dir, count_file, size_file = 0, 0, 0

print(dir_files(dir_path, size_file, count_dir, count_file))
print(os_walk(dir_path, size_file, count_dir, count_file))

# print('Размер каталога (в Кб):', size_file)
# print('Количество подкаталогов:', count_dir)
# print('Количество файлов:', count_file)
