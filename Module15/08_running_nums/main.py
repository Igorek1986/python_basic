count = int(input('Длинна списка: '))
number_list = []


for i in range(count):
    number = int(input('Введите число: '))
    number_list.append(number)


K = int(input('Сдвиг: '))
print('Изначальный список:', number_list)

a = number_list[count - K]

for k in range(1, K):
    for i in range(len(number_list)):
        number_list[count - i - 1] = number_list[count - i - 2]

# for i in range(len(number_list) - 1):
#     number_list[count - i - K] = number_list[count - i - K - 1]
#     # for i2 in range(len(number_list) - 1):
#     #     # number_list[i] = number_list[i + K] #= number_list[count - i - K], number_list[i]
#     #     break
number_list[0] = a

print('Сдвинутый список:', number_list)
# print('Сдвинутый список:', change_number_list)


#  таким образом в изначальном списке сдвиг не происходит.
#  Предлагаю попробовать решить задание без дополнительного списка и производить сдвиг сразу в начальном списке,
#  который получился после ввода пользователя.
#  Возможно сможем решить вложенными циклами.

# TODO, таким образом, начальный список немного поменялся.
#  Сдвиг: 3
#  Изначальный список: [1, 2, 3, 4, 5]
#  Сдвинутый список: [3, 4, 5, 3, 4]