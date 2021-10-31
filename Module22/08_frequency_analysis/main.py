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

    # TODO, предлагаю возвращать из данной функции не словарь, а отсортированный список.
    #  Т.к. при создании словаря, сортировка может сбиться, т.к. словарь, сортирует данные самостоятельно,
    #  для быстрого поиска значений по их ключам.
    cont_letter_dict = dict(sorted(cont_letter_dict.items(), key=lambda items: (items[1] * -1, items[0])))
    return count, cont_letter_dict


with open('text.txt', 'r') as text:
    total_letter, count_letter_analysis = count_letter_text(text)
    for key, value in count_letter_analysis.items():
        analysis_letter = round(value / total_letter, 3)
        file_answer = open('analysis.txt', 'a+')
        file_answer.write(f'{key}: {analysis_letter} \n')
    file_answer.seek(0)
    print('Содержимое файла analysis.txt:')
    print(*file_answer)
    file_answer.close()
