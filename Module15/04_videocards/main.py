NVIDIA_list = []
new_NVIDIA_list = []
number = int(input('Кол-во видеокарт: '))
num_max = 0

for i in range(number):
    graphics_card = int(input(str(i + 1) + ' Видеокарта: '))
    NVIDIA_list.append(graphics_card)
    if num_max <= NVIDIA_list[i]:
        num_max = NVIDIA_list[i]


for i in range(number):
    if NVIDIA_list[i] != num_max:
        new_NVIDIA_list.append(NVIDIA_list[i])


print('\nтарый список видеокарт:', NVIDIA_list)
print('Новый список видеокарт:', new_NVIDIA_list)
