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


def count_alphabet(cur_path, count=0, lines=0, words=0, letter_dict={}):
    with open(cur_path, 'r') as file:
        for i_line in file.readlines():
            lines += 1
            words += len(i_line.split())
            for letter in i_line:
                if letter.isalpha():
                    count += 1
            for alpha in i_line.lower():
                if alpha.isalpha() and alpha in letter_dict:
                    letter_dict[alpha] += 1
                elif alpha.isalpha():
                    letter_dict[alpha] = 1
    min_alpha = (min(letter_dict.keys(), key=(lambda key: letter_dict[key])))
    return count, lines, words, min_alpha


path_search = os.path.abspath(os.path.join('..'))
file_name = 'zen.txt'


result_path = find_file(path_search, file_name)
count_letter, count_lines, count_words, min_alpha_text = count_alphabet(result_path)


print('Количество букв:', count_letter)
print('Количество линий:', count_lines)
print('Количество слов:', count_words)
print('Буква которая встречается в тексте наименьшее количество раз:', min_alpha_text)

# Количество букв: 652
# Количество линий: 19
# Количество слов: 136
