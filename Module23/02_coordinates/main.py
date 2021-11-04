import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            # TODO, таким образом, если первая функция выдаёт ошибку, во вторую не зайдём. Но должны.
            # TODO, Предлагаю попробовать реализовать 2 пары блоков try/except для каждой функции отдельный,
            #  На одном уровне, друг за другом, и запускать наши функции внутри них.

            # TODO, если функции отработали с ошибкой, предлагаю создавать переменные res1 и res2 в блоках except
            #  со значение по умолчанию, к примеру "0".
            #  Таким образом, мы сможем избежать ошибок в коде ниже, в строке с сортировкой.

            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            with open('result.txt', 'w') as file_2:
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join(str(my_list)))
except ValueError:
    print("Что-то пошло не так проверьте значения в файле")
