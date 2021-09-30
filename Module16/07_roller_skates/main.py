skates_size = []
foot_size = []
count_skates = int(input('Кол-во коньков: '))

for i_skates in range(1, count_skates + 1):
    skates_size.append(int(input('Размер ' + str(i_skates) + ' пары: ')))

count_people = int(input('\nКол-во людей: '))

for i_people in range(1, count_people + 1):
    foot_size.append(int(input('Размер ' + str(i_people) + ' ноги: ')))

for i in range(len(foot_size)):
    for i2 in range(len(skates_size)):
        if foot_size[i] <= skates_size[i2]:
            skates_size.remove(skates_size[i2])
            break
print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_skates - len(skates_size))

# зачёт!
