def reverse(num_list):
    index = len(num_list) - 1
    for i in range((len(num_list) - 1) // 2):
        temp = num_list[index]
        num_list[index] = num_list[i]
        num_list[i] = temp
        index -= 1
        return num_list


count = int(input('Длинна списка: '))
number_list = []
revers_list = []

for i in range(count):
    number = int(input('Введите число: '))
    number_list.append(number)

revers_list.extend(number_list)
revers_list = reverse(revers_list)


print(number_list)
print(revers_list)


for i in range(1, 5):
    if number_list[-i] == revers_list[i]:
        print('число', i)
        break
    else:
        number_list.remove(number_list[i])
        revers_list.remove(revers_list[i])
