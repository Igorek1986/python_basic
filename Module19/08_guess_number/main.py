max_number = int(input('Введите максимальное число: '))

guess_number = set({str(x) for x in range(1, max_number + 1)})
numbers = input('\nНужное число есть среди вот этих чисел: ').split()
person_number = set(numbers)

# TODO Предлагаю сократить количество повторяющихся строк кода с запросом ввода пользователя до одной.
#  Стоит попробовать реализовать цикл while True и запрашивать данные только в цикле.
#  В текущей реализации нарушается принцип программирования DRY (Don`t Repeat yourself).


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
# TODO, по идее "Помогите!" мы ждём от пользователя => numbers может быть или числом или текстом. =)
# Нужное число есть среди вот этих чисел: Помогите!
# Ответ Артёма: Помогите!
#
# Ошибка ввода Артема. Ответ должен быть Yes or No
# Ответ Артёма:
