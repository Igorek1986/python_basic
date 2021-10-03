import random

num_sticks = 10 #int(input('Кол-во палок: '))
num_throw = 3 #int(input('Кол-во бросков: '))

# R_i = [random.randint(1, num_sticks) for _ in range(num_throw)]
# L_i = [random.randint(1, num_sticks) for _ in range(num_throw)]
result = ['I' * num_sticks]
print(result)
# L_i, R_i = [R_i[i] if R_i[i] < L_i[i] else L_i[i] for i in range(len(L_i))], \
#            [L_i[i] if R_i[i] < L_i[i] else R_i[i] for i in range(len(R_i))]
L_i = [8, 2, 3]
R_i = [10, 5, 6]
throw = [print('Бросок ' + str(i+1) + '. Сбиты палки с номера ' + str(L_i[i]) +
               ' по номер ' + str(R_i[i])) for i in range(num_throw)]


result = ['.' if L_i[i] <= R_i[i]
         else 'I' for i in range(len(result))]

print(result)
print(L_i)
print(R_i)

#1≤ L_i≤ R_i≤ N