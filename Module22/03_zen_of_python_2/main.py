import os


def find_file(cur_path, search_obj):
    if os.path.exists(cur_path):
        if os.path.isdir(cur_path):
            for i_elem in os.listdir(cur_path):
                path = os.path.join(cur_path, i_elem)
                if i_elem == search_obj:
                    return path
                else:
                    result = find_file(path, search_obj)
                    if result:
                        break
            else:
                result = None
            return result
    else:
        print('Файла в данной директории нет')


def count_alphabet(cur_path, count=0, lines=0, words=0):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
               'abcdefghijklmnopqrstuvwxyz'
    file = open(cur_path, 'r')
    for i_line in file:
        count += sum(1 for alpha in i_line if alpha in alphabet)
        lines += 1
        flag = True
        for letter in i_line:
            if letter != ' ' and flag:
                words += 1
                flag = False
            else:
                flag = True
    file.close()
    return count, lines, words


path_search = os.path.abspath(os.path.join('..'))
file_name = 'zen.txt'


result_path = find_file(path_search, file_name)
count_alp = count_alphabet(result_path)
print('Количество букв:', count_alp[0])
print('Количество линий:', count_alp[1])
print('Количество слов:', count_alp[2])
