def winners_tour(string):
    stop = len(string)
    for i in range(stop):
        name = str(string[i][1][:1]) + '.'
        surname = str(string[i][0])
        score = str(string[i][-1])
        string[i] = ''.join(f'{i + 1}) {name} {surname} {score} \n')


data = []
with open('first_tour.txt', 'r') as file:
    min_score = file.readline()
    for i_line in file:
        if i_line.split()[2] > min_score:
            data.append(i_line.strip('\n').split())

data.sort(key=lambda key: key[2], reverse=True)
winners_tour(data)
print('Содержимое файла second_tour.txt:')
with open('second_tour.txt', 'w+') as file_winners:
    file_winners.write(str(len(data)) + '\n')
    file_winners.writelines(data)
    file_winners.seek(0)
    print(*file_winners)
    # for i_line in file_winners:
    #     print(i_line, end='')

# зачёт!
