def revers(number):
    number = float(number)
    number = int(number)
    revers_number = 0
    while number > 0:
        last_number = number % 10
        revers_number = (revers_number * 10) + last_number
        number //= 10
    return revers_number


def symbol(number):
    number_1 = ''
    flag = True
    for line in number:
        if flag:
            if line == '.':
                flag = False
        else:
            number_1 += line
    return number_1

first_n = input('\nВведите первое число: ')
second_n = input("\nВведите второе число: ")

first_number_2 = symbol(first_n)
second_number_2 = symbol(second_n)

first_revers_number_1 = revers(first_n)
second_revers_number_1 = revers(second_n)

first_revers_number_2 = revers(first_number_2)
second_revers_number_2 = revers(second_number_2)

summa_1 = first_revers_number_1 + second_revers_number_1
summa_2 = first_revers_number_2 + second_revers_number_2

print('Первое число наоборот: ' + str(first_revers_number_1) + '.' + str(first_revers_number_2))
print('Второе число наоборот: ' + str(second_revers_number_1) + '.' + str(second_revers_number_2))
print('Сумма: ' + str(summa_1) + '.' + str(summa_2))

