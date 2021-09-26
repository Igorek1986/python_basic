unsorted_list = [1, 4, -3, 0, 10, -127]
print('Изначальный список:', unsorted_list)
for i in range(len(unsorted_list) - 1):
    for i2 in range(len(unsorted_list) - 1 - i):
        if unsorted_list[i2] > unsorted_list[i2 + 1]:
            unsorted_list[i2], unsorted_list[i2 + 1] = unsorted_list[i2 + 1], unsorted_list[i2]

print('Отсортированный список:', unsorted_list)

# зачёт!

#Разбор ДЗ

def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]


nums = [1, 4, -3, 0, 10, -127]
selection_sort(nums)
print(nums)