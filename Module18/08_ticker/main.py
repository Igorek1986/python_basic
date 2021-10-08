def shift(lst):
    first_item = lst[-1]
    for i in range(len(lst) - 2, -1, -1):
        lst[i + 1] = lst[i]
    lst[0] = first_item


first_lst = list('abcd')  # list(input('Первая строка: '))
second_list = list('cdab')  # list(input('Вторая строка: '))
count = 0

while True:
    if first_lst == second_list:
        print('\nПервая строка получается из второй со сдвигом', count)
        break
    elif count > len(first_lst):
        print('\nПервую строку нельзя получить из второй с помощью циклического сдвига')
        break
    else:
        shift(second_list)
        count += 1

# зачёт!
