count_friends = int(input('Кол-во друзей: '))
count_debt = int(input('Долговых расписок: '))
friend_list = [0, 0, 0]

for i in range(1, count_debt + 1):
    print()
    print(i, 'расписка')
    to_people = int(input('Кому: '))
    from_people = int(input('От кого: '))
    if to_people != from_people:
        money = int(input('Сколько: '))
        friend_list[to_people - 1] = -money + friend_list[to_people - 1]
        friend_list[from_people - 1] = money + friend_list[from_people - 1]
    else:
        print('Самому себе занимать нельзя!')
print('\nБаланс друзей:')
for i in range(1, count_friends + 1):
    print(str(i), ' :', friend_list[i - 1])
