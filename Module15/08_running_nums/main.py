count = int(input('Длинна списка: '))
number_list = []
change_number_list = []


for i in range(count):
    number = int(input('Введите число: '))
    number_list.append(number)


K = int(input('Сдвиг: '))


for i in range(count):
    change_number_list.append(number_list[i - K])

print('Изначальный список:', number_list)
print('Сдвинутый список:', change_number_list)

# TODO, таким образом в изначальном списке сдвиг не происходит.
#  Предлагаю попробовать решить задание без дополнительного списка и производить сдвиг сразу в начальном списке,
#  который получился после ввода пользователя.
#  Возможно сможем решить вложенными циклами.
