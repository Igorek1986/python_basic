line_count = 0
summ_sym = 0
with open('people.txt', 'r', encoding='utf-8') as file:
    for i_line in file.readlines():
        line_count += 1
        length = len(i_line.strip('\n'))
        try:
            if length < 3:
                raise ValueError
        except ValueError:
            with open('errors.log', 'w') as error:
                error.write(f'Ошибка в строке {line_count}')
            print(f'Ошибка в строке {line_count}')
        summ_sym += length

print('Кол-во символов в файле:', summ_sym)
