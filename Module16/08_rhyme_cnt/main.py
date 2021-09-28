count_number = int(input('Какое число в считалке? '))
count_people = int(input('Кол-во человек: '))
people = list(range(1, count_people + 1))
print('Значит, выбывает каждый', count_number, 'человек\n')
out_circle = 0


for i in range(count_people - 1):
    print('Текущий круг людей: ', people)
    start = out_circle % len(people)
    out_circle = (start + count_number - 1) % len(people)
    print('Начало счёта с номера', people[start])
    print('Выбывает человек под номером', people[out_circle], '\n')
    people.remove(people[out_circle])
