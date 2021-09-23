def revers(number):
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
            return number_2


first_n = input('\nВведите первое число: ')
second_n = input("\nВведите второе число: ")
a = first_n = int(first_n)
print(a)
b = int(second_n)


#  для сокращения количества кода в текущем задании, предлагаю написать ещё одну функцию.
#  Вне функций должен остаться только код с запросом ввода пользователя и вызовом функций. =)


# symbol = '.'
# first_number_1 = ''
# first_number_2 = ''
# flag = True
# for line in first_n:
#     if flag:
#         if line != '.':
#             first_number_1 += line
#         elif line == '.':
#             flag = False
#     else:
#         first_number_2 += line
#
# symbol = '.'
# second_number_1 = ''
# second_number_2 = ''
# flag = True
# for line in second_n:
#     if flag:
#         if line != '.':
#             second_number_1 += line
#         elif line == '.':
#             flag = False
#     else:
#         second_number_2 += line


# first_number_1 = symbol(first_n)
first_number_2 = symbol(first_n)
# second_number_1 = symbol(second_n)
second_number_2 = symbol(second_n)

first_revers_number_1 = revers(a)
second_revers_number_1 = revers(b)


# first_revers_number_1 = revers(first_n)
# second_revers_number_1 = revers(second_n)

first_revers_number_2 = revers(first_number_2)
second_revers_number_2 = revers(second_number_2)

summa_1 = first_revers_number_1 + second_revers_number_1
summa_2 = first_revers_number_2 + second_revers_number_2

print('Первое число наоборот: ' + str(first_revers_number_1) + '.' + str(first_revers_number_2))
print('Второе число наоборот: ' + str(second_revers_number_1) + '.' + str(second_revers_number_2))
print('Сумма: ' + str(summa_1) + '.' + str(summa_2))

