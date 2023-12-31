import os


def gen_files_path(path: str) -> int:
    for dirs, folder, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                count = count_str_code(os.path.join(dirs, file))
                yield count, os.path.join(dirs, file)


def count_str_code(files: str) -> int:
    with open(files, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if line.split() and not line.startswith('#'):
                count += 1
    return count


path_user = input('Введите путь через пробел: ').split()
root_path = os.path.abspath(os.path.join(os.path.sep, *path_user))
dirs_search = gen_files_path(path=root_path)
count_code = 0

for i_count, i_file in dirs_search:
    count_code += i_count

print('Количество строк кода:', count_code)

# Users Igor Documents Skillbox Module25
# Module25
# 382

# зачёт!
