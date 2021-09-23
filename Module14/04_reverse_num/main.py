def revers(number):
    revers_number = 0
    while number > 0:
        last_number = number % 10
        revers_number = (revers_number * 10) + last_number
        number //= 10
    return revers_number


first_n = input('\nВведите первое число: ')
second_n = input("\nВведите второе число: ")


symbol = '.'
first_number_1 = ''
first_number_2 = ''
flag = True
for line in first_n:
    if flag:
        if line != '.':
            first_number_1 += line
        elif line == '.':
            flag = False
    else:
        first_number_2 += line

symbol = '.'
second_number_1 = ''
second_number_2 = ''
flag = True
for line in second_n:
    if flag:
        if line != '.':
            second_number_1 += line
        elif line == '.':
            flag = False
    else:
        second_number_2 += line


first_number_1 = int(first_number_1)
first_number_2 = int(first_number_2)
second_number_1 = int(second_number_1)
second_number_2 = int(second_number_2)

first_revers_number_1 = revers(first_number_1)
first_revers_number_2 = revers(first_number_2)

second_revers_number_1 = revers(second_number_1)
second_revers_number_2 = revers(second_number_2)

summa_1 = first_revers_number_1 + second_revers_number_1
summa_2 = first_revers_number_2 + second_revers_number_2

print('Первое число наоборот: ' + str(first_revers_number_1) + '.' + str(first_revers_number_2))
print('Второе число наоборот: ' + str(second_revers_number_1) + '.' + str(second_revers_number_2))
print('Сумма: ' + str(summa_1) + '.' + str(summa_2))

