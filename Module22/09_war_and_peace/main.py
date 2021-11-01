import zipfile


def count_letter_text(file, cont_letter_dict={}):
    for i_line in file:
        for letter in i_line:
            if letter.isalpha() and letter in cont_letter_dict:
                cont_letter_dict[letter] += 1
            elif letter.isalpha():
                cont_letter_dict[letter] = 1
    cont_letter_dict = sorted(cont_letter_dict.items(), key=lambda items: (items[1], items[0]))
    return cont_letter_dict


with zipfile.ZipFile('voyna-i-mir.zip', 'r') as file_zip:
    file_zip.extractall()

with open('voyna-i-mir.txt', 'r', encoding='utf-8') as text:
    count_letter_analysis = count_letter_text(text)
    for i in range(len(count_letter_analysis)):
        letter_analysis = count_letter_analysis[i][0]
        letter_analysis_count = count_letter_analysis[i][1]
        file_answer = open('analysis_text.txt', 'a+', encoding='utf-8')
        file_answer.write(f'{letter_analysis}: {letter_analysis_count} \n')
    file_answer.seek(0)
    print('Содержимое файла analysis_text.txt:')
    print(*file_answer)
    file_answer.close()

# зачёт!


# Parsing homework
# import collections
# import zipfile
#
#
# def unzip(archive):
#     zfile = zipfile.ZipFile(archive, 'r')
#     for i_file_name in zfile.namelist():
#         zfile.extract(i_file_name)
#     zfile.close()
#
#
# def collect_stats(file_name):
#     result = {}
#     if file_name.endswith('.zip'):
#         unzip(file_name)
#         file_name = ''.join((file_name[:-3], 'txt'))
#     text_file = open(file_name, 'r', encoding='utf-8')
#     for i_line in text_file:
#         for j_char in i_line:
#             if j_char.isalpha():
#                 if j_char not in result:
#                     result[j_char] = 0
#                 result[j_char] += 1
#     text_file.close()
#
#     return result
#
#
# def print_stats(stats):
#     print("+{:-^19}+".format('+'))
#     print("|{: ^9}|{: ^9}|".format('буква', 'частота'))
#     print("+{:-^19}+".format('+'))
#     for char, count in stats.items():
#         print("|{: ^9}|{: ^9}|".format(char, count))
#     print("+{:-^19}+".format('+'))
#
#
# def sort_by_frequency(stats_dict):
#     sorted_values = sorted(stats_dict.values())
#     sorted_dict = collections.OrderedDict()
#     for i_value in sorted_values:
#         for j_key in stats_dict.keys():
#             if stats_dict[j_key] == i_value:
#                 sorted_dict[j_key] = stats_dict[j_key]
#
#     return sorted_dict
#
#
# file_name = 'voyna-i-mir.zip'
# stats = collect_stats(file_name)
# stats = sort_by_frequency(stats)
# print_stats(stats)
