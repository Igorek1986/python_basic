world = input('Введите слово: ')

# count = 0
for letter in world:
    count = 0
    for letter1 in world:
        if letter1 != letter:
            count += 1
    # print()

print(count)