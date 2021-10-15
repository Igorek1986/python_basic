def height(hum):
    if hum not in pedigree:
        return 0
    else:
        return 1 + height(pedigree[hum])


numbers = int(input('Введите количество человек: '))
pedigree = dict()
height_p = dict()


for i_numbers in range(1, numbers):
    child, parent = input(f'{i_numbers} пара: ').split()
    pedigree[child] = parent


for humans in set(pedigree.values()).union(pedigree.keys()):
    height_p[humans] = height(humans)


for key, values in sorted(height_p.items()):
    print(key, values)


# for key in sorted(height_p):
#     print(key, height_p[key])
