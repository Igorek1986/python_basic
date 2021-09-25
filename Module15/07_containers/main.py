count_container = int(input('Кол-во контейнеров: '))
weight_list = []
place = 0
count = 0
while True:
    weight_container = int(input('Введите вес контейнера: '))
    if 0 < weight_container < 200:
        count += 1
        weight_list.append(weight_container)
        if count == count_container:
            break
    else:
        print('Введен не правильный вес!')

new_weight_container = int(input('\nВведите вес нового контейнера: '))

for i in weight_list:
    place += 1
    if i < new_weight_container:
        break
print('\nНомер, куда встанет новый контейнер:', place)

# зачёт!
