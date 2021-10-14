max_number = int(input('Введите максимальное число: '))
guess_number = set({str(x) for x in range(1, max_number + 1)})

while True:
    numbers = set(input('\nНужное число есть среди вот этих чисел: ').split())
    if numbers != set('Помогите!'.split()):
        answer = input('Ответ Артёма: ')
        if answer == 'Yes':
            guess_number = guess_number.intersection(numbers)
            if len(guess_number) == 1:
                break
        elif answer == 'No':
            guess_number = guess_number.difference(numbers)
        else:
            print('\nОшибка ввода Артема. Ответ должен быть Yes or No')
    else:
        break

print('\nАртём мог загадать следующие числа:', end=' ')
for num in sorted(guess_number):
    print(num, end=' ')

# Введите максимальное число: 5
#
# Нужное число есть среди вот этих чисел: 1 2
# Ответ Артёма: No
#
# Нужное число есть среди вот этих чисел: 3 4
# Ответ Артёма: Yes
#
# Нужное число есть среди вот этих чисел: 3
# Ответ Артёма: No
#
# Нужное число есть среди вот этих чисел: 4
# Ответ Артёма: Yes
#
# Нужное число есть среди вот этих чисел: Помогите!
# Ответ Артёма: Помогите!
#
# Ошибка ввода Артема. Ответ должен быть Yes or No
# Ответ Артёма:


# зачёт!
