import os


def gen_files_path(user_dir: str) -> str:
    path = os.path.abspath(os.path.join('/'))
    for dirs, folder, files in os.walk(path):

        if user_dir in dirs:
            for file in files:
                yield os.path.join(dirs, file)


dirs = gen_files_path('Module26')
for i_path in dirs:
    print(i_path)
