def sorted_tour(string):
    string = string.split()
    name = str(string[-2][:1]) + '.'
    surname = str(string[0])
    score = str(string[-1])
    return ' '.join((name, surname, score))



data = []
with open('first_tour.txt', 'r') as file:
    min_score = file.readline()
    for i_line in file:
        if not i_line.split()[-1] < min_score:
            sort_score = sorted_tour(i_line)
            data.append(sort_score)




    print(data)
