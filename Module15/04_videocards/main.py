NVIDIA_list = []
new_NVIDIA_list = []
number = int(input('Кол-во видеокарт: '))
num_max = 0

for i in range(number):
    graphics_card = int(input(str(i + 1) + ' Видеокарта: '))
    NVIDIA_list.append(graphics_card)
    if num_max <= graphics_card:
        num_max = graphics_card


for i in NVIDIA_list:
    if i != num_max:
        new_NVIDIA_list.append(i)


print('\nтарый список видеокарт:', NVIDIA_list)
print('Новый список видеокарт:', new_NVIDIA_list)
