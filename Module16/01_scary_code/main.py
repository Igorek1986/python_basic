def deletion(num_list, num):
    for i in num_list:
        if i == num:
            a.remove(num)

def added(num_list):
    a.extend(num_list)

a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

added(b)

print('Кол-во цифр 5 при первом объединении:', a.count(5))

deletion(a, 5)
added(c)

print('Кол-во цифр 3 при втором объединении:', a.count(3))
print('Итоговый список:', a)
#
# # for i in b:
# #     a.append(i)
# # t = 0
# # for i in a:
# #     if i == 5:
# #         t += 1
# # print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)


