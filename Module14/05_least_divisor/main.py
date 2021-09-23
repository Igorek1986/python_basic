def num_denominator(number):
    denominator = 1
    while denominator < number:
        denominator = denominator + 1
        if number % denominator == 0:
            return denominator

n = int(input('Введите число: '))
min_denominator = num_denominator(n)
print('Наименьший делитель, отличный от единицы:', min_denominator)
