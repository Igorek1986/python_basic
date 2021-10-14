numbers = int(input('Введите количество человек: '))
pedigree = dict()

for i_numbers in range(1, numbers):
    tree_element = input(f'{i_numbers} пара: ').split()
    child, parent = tree_element[0], tree_element[1]
    if parent in pedigree:
        pedigree[parent][child] = None
        if parent in pedigree[parent]:
            pedigree[parent][child] = None
        else:
            pedigree[parent] = {child: None}
    else:
        pedigree[parent] = {child: None}

print(pedigree)