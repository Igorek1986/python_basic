import random

num_sticks = 10  # int(input('Кол-во палок: '))
num_throw = 3  # int(input('Кол-во бросков: '))

R_i = [random.randint(1, num_sticks) for _ in range(num_throw)]
L_i = [random.randint(1, num_sticks) for _ in range(num_throw)]
result_list = ['I' for _ in range(num_sticks)]
result = ''

L_i, R_i = [R_i[i] if R_i[i] < L_i[i] else L_i[i] for i in range(len(L_i))], \
           [L_i[i] if R_i[i] < L_i[i] else R_i[i] for i in range(len(R_i))]
throw = [print('Бросок ' + str(i + 1) + '. Сбиты палки с номера ' + str(L_i[i]) +
               ' по номер ' + str(R_i[i])) for i in range(num_throw)]

for i in range(num_throw):
    left = int(L_i[i])
    right = int(R_i[i])
    for i2 in range(left - 1, right):
        result_list[i2] = '.'

for i in range(len(result_list)):
    result += result_list[i]

print('\nРезультат:', result)

# зачёт!
