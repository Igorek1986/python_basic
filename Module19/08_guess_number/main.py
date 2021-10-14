max_number = int(input('Введите максимальное число: '))


guess_number = set({str(x) for x in range(1, max_number + 1)})
numbers = input('\nНужное число есть среди вот этих чисел: ').split()
person_number = set(numbers)


while numbers != 'Помогите!':
    answer = input('Ответ Артёма: ')
    if answer == 'Yes':
        guess_number = guess_number.intersection(person_number)
        numbers = input('\nНужное число есть среди вот этих чисел: ').split()
        person_number = set(numbers)
    elif answer == 'No':
        guess_number = guess_number.difference(person_number)
        numbers = input('\nНужное число есть среди вот этих чисел: ')
        person_number = set(numbers)
    else:
        print('\nОшибка ввода Артема. Ответ должен быть Yes or No')

print('\nАртём мог загадать следующие числа:', end=' ')
for num in sorted(guess_number):
    print(num, end=' ')
