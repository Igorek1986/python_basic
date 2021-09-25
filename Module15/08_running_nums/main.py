count = int(input('Длинна списка: '))
number_list = []


for i in range(count):
    number = int(input('Введите число: '))
    number_list.append(number)


K = int(input('Сдвиг: '))
print('Изначальный список:', number_list)

a = number_list[count - K]

for _ in range(K):
    b = number_list[count - 1]
    for i in range(len(number_list) - 2, -1, -1):
        number_list[i + 1] = number_list[i]
    number_list[0] = b

number_list[0] = a

print('Сдвинутый список:', number_list)
