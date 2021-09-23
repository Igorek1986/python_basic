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
    number_2 = ''
    flag = True
    for line in number:
        if flag:
            if line != '.':
                number_1 += line
            elif line == '.':
                flag = False
        else:
            number_2 += line
    number_1 = revers(number_1)
    number_2 = revers(number_2)
    number = str(number_1) + '.' + str(number_2)
    return number


first_n = input('\nВведите первое число: ')
second_n = input("\nВведите второе число: ")

first_revers = symbol(first_n)
second_revers = symbol(second_n)


print('Первое число наоборот: ', first_revers)
print('Второе число наоборот: ', second_revers)
print('Сумма: ', float(first_revers) + float(second_revers))
