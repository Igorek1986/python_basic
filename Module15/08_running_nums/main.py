count = int(input('Длинна списка: '))
number_list = []


for i in range(count):
    number = int(input('Введите число: '))
    number_list.append(number)


K = int(input('Сдвиг: '))
print('Изначальный список:', number_list)


for i in range(count):
    for i2 in range(count):
        number_list[i] = number_list[i - K]
        break


print('Сдвинутый список:', number_list)
# print('Сдвинутый список:', change_number_list)


#  таким образом в изначальном списке сдвиг не происходит.
#  Предлагаю попробовать решить задание без дополнительного списка и производить сдвиг сразу в начальном списке,
#  который получился после ввода пользователя.
#  Возможно сможем решить вложенными циклами.
