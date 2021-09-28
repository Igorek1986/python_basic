skates_size = []
foot_size = []
count_skates = int(input('Кол-во коньков: '))


for i_skates in range(count_skates):
    skates_size.append(int(input('Размер ' + str(i_skates + 1) + ' пары: ')))


count_people = int(input('\nКол-во людей: '))


for i_people in range(count_people):
    foot_size.append(int(input('Размер ' + str(i_people + 1) + ' ноги: ')))


for i in range(len(foot_size)):
    a = foot_size[i]
    for i2 in range(len(skates_size)):
        b = skates_size[i2]
        if a == b:
            skates_size.remove(skates_size[i2])
            break
print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_skates - len(skates_size))