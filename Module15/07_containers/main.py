count_container = int(input('Кол-во контейнеров: '))
weight_list = []
place = 0
for i in range(count_container):
    # TODO, стоит добавить в решение цикл while True.
    #  Иначе, при некорректном вводе, вес контейнера, всё равно добавляется в список.
    weight_container = int(input('Введите вес контейнера: '))
    if 0 < weight_container < 200:
        count_container -= 1
        weight_list.append(weight_container)
    else:
        print('Введен не правильный вес!')


new_weight_container = int(input('\nВведите вес нового контейнера: '))


for i in weight_list:
    place += 1
    if i < new_weight_container:
        break
print('\nНомер, куда встанет новый контейнер:', place)
