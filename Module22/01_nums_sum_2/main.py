lst_numbers = []
file_input = open('numbers.txt', 'r', encoding='utf-8')
file_answer = open('answer.txt', 'w', encoding='utf-8')
print('Содержимое файла numbers.txt')
for i_line in file_input:
    print(i_line, end='')
    num = i_line.strip()
    if num.isdigit():
        # TODO, предлагаю попробовать решить задание без использования дополнительного списка lst_numbers.
        #  Вместо списка, стоит использовать обычную переменную счётчик.
        #  Т.к. списки занимают на порядок больше места в памяти, чем обычные числовые переменные.
        lst_numbers.append(int(num))


file_answer.write(str(sum(lst_numbers)))
file_answer.close()
file_input.close()


# TODO, предлагаю не закрывать файл перед выводом текста.
#  Стоит открыть файл один раз в режим на запись и на чтение, после чего, после записи данных в файл,
#  перенести курсор в начало файла при помощи метода seek и произвести вывод данных.
#  В таком случае, закрывать и открывать файл повторно будет не нужно.
#  Все режимы открытия файлов можно посмотреть тут:
#  http://pythonicway.com/python-fileio

file_answer = open('answer.txt', 'r')
print('Содержимое файла answer.txt')
for i_line in file_answer:
    print(i_line, end='')
file_answer.close()
