n = 10  # int(input('Введите длину списка: '))

number_list = [1 if x % 2 == 0
               else x % 5
               for x in range(n)]

print(number_list)

# зачёт!
