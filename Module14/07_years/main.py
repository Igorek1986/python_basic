def special_year(year_1, year_2):
    print('Года от ' + str(year_1) + ' до ' + str(year_2) + ' с тремя одинаковыми цифрами:')
    a = 0
    b = 0
    c = 0
    d = 0
    for line in range(year_1, year_2 + 1):
        a = line // 1000
        b = line // 100 % 10
        c = line // 10 % 10
        d = line % 10
        if (a == b == c) or (a == c == d) or (a == b == d) or (b == c == d):
            print(line)

year_1 = int(input('Введите первый год: '))
year_2 = int(input('Введите второй год: '))
special_year(year_1, year_2)





####################
#создаёт нагрузку на код
        # a = line
        # flag = False
        # while a > 0:
        #     x = a % 10
        #     a = a // 10
        #     b = line
        #     count = 0
        #     while b > 0:
        #         y = b % 10
        #         b = b // 10
        #         if x == y:
        #             count += 1
        #     if flag:
        #         break
        #     else:
        #         flag = count == 3
        # if flag:
        #     print(line)
###########################