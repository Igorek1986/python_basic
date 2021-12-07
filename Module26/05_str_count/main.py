import os


def gen_files_path(path: str, user_dir: str) -> str:
    for dirs, folder, files in os.walk(path):
        for file in files:
            if user_dir in dirs and file.endswith('.py'):
                yield os.path.join(dirs, file)


def count_str_code(files: str) -> int:
    with open(files, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if line.split() and not line.startswith('#'):
                count += 1
    return count


path_user = input('Введите путь через пробел: ').split()
root_path = os.path.abspath(os.path.join(os.path.sep, *path_user))

dirs_name = input('Введите наименование директории: ')
dirs_search = gen_files_path(path=root_path, user_dir=dirs_name)
count_code = 0

for i_path in dirs_search:
    count_code += count_str_code(i_path)

print('Количество строк кода:', count_code)

# Users Igor Documents Skillbox
# Module25
