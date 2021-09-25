world = input('Введите слово: ')
flag = False

for i in range(len(world) // 2):
    if world[i] != world[-1 - i]:
        print('\nСлово не является палиндромом')
        break
    else:
        flag = True

if flag == True:
    print('\nСлово является палиндромом')

# зачёт!
