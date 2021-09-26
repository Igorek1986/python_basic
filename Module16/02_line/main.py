def line_class(class_list, num1, num2, num3):
    class_list.extend(list(range(num1, num2 + 1, num3)))


def selection_sort(class_list):
    for i_mx in range(len(class_list)):
        for curr in range(len(class_list)):
            if class_list[curr] > class_list[i_mx]:
                class_list[curr], class_list[i_mx] = class_list[i_mx], class_list[curr]


class_a = []
class_b = []
line_class(class_a, 160, 176, 2)
line_class(class_b, 162, 180, 3)


print('\nПервый класс', class_a)
print('Второй класс', class_b)


class_a.extend(class_b)
selection_sort(class_a)


print('\nОбъединенный класс', class_a)
