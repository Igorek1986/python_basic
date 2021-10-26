lst_numbers = []
file_input = open('numbers.txt', 'r', encoding='utf-8')
file_answer = open('answer.txt', 'w', encoding='utf-8')
print('Содержимое файла numbers.txt')
for i_line in file_input:
    print(i_line, end='')
    num = i_line.strip()
    if num.isdigit():
        lst_numbers.append(int(num))


file_answer.write(str(sum(lst_numbers)))
file_answer.close()
file_input.close()


file_answer = open('answer.txt', 'r')
print('Содержимое файла answer.txt')
for i_line in file_answer:
    print(i_line, end='')
file_answer.close()
