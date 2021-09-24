numbers_list = []
n = int(input('Введите число: '))


# TODO, пожалуйста, обратите внимание, в список ниже, необходимо добавить только нечётные числа.
#  Стоит немного поправить range и добавить в него шаг.
for i in range(0, n + 1):
    numbers_list.append(i)
print(numbers_list)
