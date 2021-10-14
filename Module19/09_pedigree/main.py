def height(humans):
    if humans not in pedigree:
        return 0
    else:
        return 1  # TODO, в этот возврат стоит прибавить вызов нашей функции, передав в него словарь pedigree с ключом humans


numbers = int(input('Введите количество человек: '))
pedigree = dict()
height_p = dict()

for i_numbers in range(1, numbers):
    child, parent = input(f'{i_numbers} пара: ').split()
    pedigree[child] = parent


for humans in set(pedigree.values()).union(pedigree.keys()):
    height_p[humans] = height(humans)


print(height_p)

# TODO, пожалуйста, реализуйте вывод как в примере.