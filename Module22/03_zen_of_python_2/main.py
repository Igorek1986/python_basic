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
    with open(cur_path, 'r') as file:
        for i_line in file.readlines():
            lines += 1
            words += len(i_line.split())
            for letter in i_line:
                if letter.isalpha():
                    count += 1
    return count, lines, words


def min_alpha_text(cur_path, letter_dict={}):
    with open(cur_path, 'r') as file:
        for i_line in file:
            for alpha in i_line.lower():
                if alpha.isalpha() and alpha in letter_dict:
                    letter_dict[alpha] += 1
                elif alpha.isalpha():
                    letter_dict[alpha] = 1
    min_letter_count = min(letter_dict.values())
    min_alpha = [i_keys for i_keys, i_value in letter_dict.items() if i_value == min_letter_count]
    return min_alpha


path_search = os.path.abspath(os.path.join('..'))
file_name = 'zen.txt'

# TODO, предлагаю уйти от использования функции min_alpha_text.
#  Словарь с подсчётом данных стоит реализовать внутри функции count_alphabet.
#  Таким образом, мы сможем сократить количество циклов в нашем коде.
#  После чего, словарь с данными, стоит передать в функцию min.
#  Если подобрать подходящую lambda функцию, то, найти букву с минимальным количеством повторений, мы сможем в одну строку кода. =)

result_path = find_file(path_search, file_name)
count_alp = count_alphabet(result_path)
alpha_min = min_alpha_text(result_path)

# TODO, создать несколько переменных из одного возврата функции, можно следующим образом
#  a, b = func()

print('Количество букв:', count_alp[0])
print('Количество линий:', count_alp[1])
print('Количество слов:', count_alp[2])
print('Буква которая встречается в тексте наименьшее количество раз:', str(alpha_min[0]))

# Количество букв: 652
# Количество линий: 19
# Количество слов: 136
