def winners_tour(string):
    stop = len(string)
    for i in range(stop):
        name = str(string[i][1][:1]) + '.'
        surname = str(string[i][0])
        score = str(string[i][-1])
        string[i] = ' '.join((name, surname, score + '\n'))


data = []
with open('first_tour.txt', 'r') as file:
    min_score = file.readline()
    for i_line in file:
        if i_line.split()[2] > min_score:
            data.append(i_line.strip('\n').split())

data.sort(key=lambda key: key[2], reverse=True)
winners_tour(data)
print(data)
with open('second_tour.txt', 'w') as file_winners:
    file_winners.writelines(data)

# TODO, пожалуйста, обратите внимание на условие задания
#  "В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. "