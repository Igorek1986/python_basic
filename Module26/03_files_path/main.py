import os


def gen_files_path(path: str, user_dir: str) -> str:
    for dirs, folder, files in os.walk(path):
        for file in files:
            yield os.path.join(dirs, file)
            if user_dir in dirs:
                return


path_user = input('Введите путь через пробел: ').split()
root_path = os.path.abspath(os.path.join(os.path.sep, *path_user))

dirs_name = input('Введите наименование директории: ')
dirs_search = gen_files_path(path=root_path, user_dir=dirs_name)
for i_path in dirs_search:
    print(i_path)


# Users Igor Documents Skillbox
# 04_hof_seq
