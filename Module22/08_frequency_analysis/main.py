def count_letter_text(file, count=0, cont_letter_dict={}):
    for i_line in file:
        for alpha in i_line:
            if alpha.isalpha():
                count += 1
        for letter in i_line.lower():
            if letter.isalpha() and letter in cont_letter_dict:
                cont_letter_dict[letter] += 1
            elif letter.isalpha():
                cont_letter_dict[letter] = 1
    cont_letter_dict = sorted(cont_letter_dict.items(), key=lambda items: (items[1] * -1, items[0]))
    return count, cont_letter_dict


with open('text.txt', 'r') as text:
    total_letter, count_letter_analysis = count_letter_text(text)
    for i in range(len(count_letter_analysis)):
        analysis_letter = count_letter_analysis[i][0]
        analysis_letter_count = round(count_letter_analysis[i][1] / total_letter, 3)
        file_answer = open('analysis.txt', 'a+')
        file_answer.write(f'{analysis_letter}: {analysis_letter_count} \n')
    file_answer.seek(0)
    print('Содержимое файла analysis.txt:')
    print(*file_answer)
    file_answer.close()

# зачёт!
