NVIDIA_list = []
new_NVIDIA_list = []
number = int(input('Кол-во видеокарт: '))
num_max = 0

for i in range(number):
    graphics_card = int(input(str(i + 1) + ' Видеокарта: '))
    NVIDIA_list.append(graphics_card)
    # TODO, для сокращения количества вычислений по индексам, в коде ниже,
    #  предлагаю сравнивать максимальное число с вводом пользователя graphics_card.
    if num_max <= NVIDIA_list[i]:
        num_max = NVIDIA_list[i]

# TODO, предлагаю уйти от вычислений элементов по их индексам и в цикле ниже, идти сразу по списку видеокарт. =)
for i in range(number):
    if NVIDIA_list[i] != num_max:
        new_NVIDIA_list.append(NVIDIA_list[i])


print('\nтарый список видеокарт:', NVIDIA_list)
print('Новый список видеокарт:', new_NVIDIA_list)
