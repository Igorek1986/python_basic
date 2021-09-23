def summ_number(n):
    summ_n = 0
    while n != 0:
        last_num = n % 10
        summ_n += last_num
        n //= 10
    return summ_n


def count_number(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count


n = int(input('Введите число: '))
summ_number(n)
count_number(n)

summa = summ_number(n)
count = count_number(n)
print('Сумма цифр:', summa)
print('Кол-во цифр в числе:', count)
print('Разность суммы и кол-ва цифр:', summa - count)

# зачёт!
