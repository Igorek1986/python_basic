count_friends = int(input('Кол-во друзей: '))
count_debt = int(input('Долговых расписок: '))
friend_list = []

for _ in range(0, count_debt + 1):
    print('\n', count_debt, 'расписка')
    to_people = int(input('Кому: '))
    from_people = int(input('От кого: '))
    money = int(input('Сколько: '))
    if to_people == 1:
