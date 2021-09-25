unsorted_list = [1, 4, -3, 0, 10, -127]
print('Изначальный список:', unsorted_list)
for i in range(len(unsorted_list) - 1):
    for i2 in range(len(unsorted_list) - 1 - i):
        if unsorted_list[i2] > unsorted_list[i2 + 1]:
            unsorted_list[i2], unsorted_list[i2 + 1] = unsorted_list[i2 + 1], unsorted_list[i2]

print('Отсортированный список:', unsorted_list)

# зачёт!
