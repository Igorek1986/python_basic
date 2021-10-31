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
