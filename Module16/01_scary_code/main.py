def deletion(num_list, num):
    for i in range(num_list.count(num)):
        num_list.remove(num)


def added(num_list):
    main_list.extend(num_list)


main_list = [1, 5, 3]
side_list_1 = [1, 5, 1, 5]
side_list_2 = [1, 3, 1, 5, 3, 3]


added(side_list_1)

print('Кол-во цифр 5 при первом объединении:', main_list.count(5))

deletion(main_list, 5)
added(side_list_2)

print('Кол-во цифр 3 при втором объединении:', main_list.count(3))
print('Итоговый список:', main_list)
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
