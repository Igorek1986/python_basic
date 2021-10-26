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

# TODO, предлагаю упростить решение и попробовать решить задание за пару вложенных циклов.
#  В таком случае, мы сможем сократить количество циклов в коде, что снизит нагрузку на код и количество функций. =)

def hist_dict(cur_path, letter_dict={}):
    # TODO, переменная alphabet возможно, получилась лишней.
    #  Предлагаю использовать в решении строковой метод isalpha. =)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
               'abcdefghijklmnopqrstuvwxyz'
    file = open(cur_path, 'r')
    for i_line in file:
        for alpha in i_line.lower():
            if alpha in alphabet and alpha in letter_dict:
                letter_dict[alpha] += 1
            elif alpha in alphabet:
                letter_dict[alpha] = 1
    file.close()
    min_letter_count = min(letter_dict.values())
    return letter_dict, min_letter_count


def inverted(dct):
    inverted_dict = dict()
    for i_key in dct:
        if dct[i_key] in inverted_dict:
            inverted_dict[dct[i_key]].append(i_key)
        else:
            inverted_dict[dct[i_key]] = [i_key]
    return inverted_dict


path_search = os.path.abspath(os.path.join('..'))
file_name = 'zen.txt'


result_path = find_file(path_search, file_name)
count_alp = count_alphabet(result_path)
print('Количество букв:', count_alp[0])
print('Количество линий:', count_alp[1])
print('Количество слов:', count_alp[2])
alphabet_dict = hist_dict(result_path)
result_dict = inverted(alphabet_dict[0])

min_alpha = ' '.join(result_dict[alphabet_dict[1]])
print('Буква которая встречается в тексте наименьшее количество раз:', str(min_alpha))
