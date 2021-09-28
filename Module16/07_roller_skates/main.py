skates_size = []
foot_size = []
count_skates = int(input('Кол-во коньков: '))

# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
#  В таком случае, вычисление произойдёт только 1 раз в range, вместо вычислений каждую итерацию цикла.
for i_skates in range(count_skates):
    skates_size.append(int(input('Размер ' + str(i_skates + 1) + ' пары: ')))


count_people = int(input('\nКол-во людей: '))


for i_people in range(count_people):
    foot_size.append(int(input('Размер ' + str(i_people + 1) + ' ноги: ')))


for i in range(len(foot_size)):
    a = foot_size[i]
    for i2 in range(len(skates_size)):
        b = skates_size[i2]
        if a == b:  # TODO, размер коньков может быть больше размера ноги человека =)
            skates_size.remove(skates_size[i2])  # TODO, удалять можно сразу переменную "b".
            break
print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_skates - len(skates_size))