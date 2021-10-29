import os


def os_walk(cur_path, size_dirs=0, sub_dirs_count=0, files_count=0):
    if os.path.exists(cur_path):
        for cur_path, dir_names, filenames in os.walk(cur_path):
            for _ in dir_names:
                sub_dirs_count += 1
            for filename in filenames:
                if filename != '.DS_Store':
                    size_dirs += (os.path.getsize(os.path.join(cur_path, filename)) / 1024)
                    files_count += 1
    else:
        print('Не верно указана директория')
    return size_dirs, sub_dirs_count, files_count


def dir_files(cur_path, size_dirs=0, sub_dirs_count=0, files_count=0):
    if os.path.exists(cur_path):
        for i_elem in os.listdir(cur_path):
            path = os.path.join(cur_path, i_elem)
            if os.path.isfile(path) and i_elem != '.DS_Store':
                files_count += 1
                size_dirs += os.path.getsize(path) / 1024
            if os.path.isdir(path):
                sub_dirs_count += 1
                size_dirs, sub_dirs_count, files_count = dir_files(path, size_dirs, sub_dirs_count, files_count)
        return size_dirs, sub_dirs_count, files_count
    else:
        print('Не верно указана директория')
    return size_dirs, sub_dirs_count, files_count


dir_path = os.path.abspath(os.path.join('..', '..', 'Module14'))
dir_info = dir_files(dir_path)

print('Размер каталога (в Кб):', dir_info[0])
print('Количество подкаталогов:', dir_info[1])
print('Количество файлов:', dir_info[2])

# зачёт! Молодец!
