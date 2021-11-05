def write_bad_log(string, error):
    with open('registrations_bad.log', 'a', encoding='utf-8') as bad:
        bad.write(f'{string.rstrip()} - {error}\n')


count_line = 0
with open('registrations.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        count_line += 1
        my_list = list(line.split())
        try:
            if len(my_list) < 3:
                raise IndexError
            if not my_list[0].isalpha():
                raise NameError
            if not '@' in my_list[1] and not '.' in my_list[1]:
                raise SyntaxError
            if not 10 < int(my_list[2]) < 99:
                raise ValueError
        except IndexError:
            write_bad_log(line, IndexError)
        except NameError:
            write_bad_log(line, NameError)
        except SyntaxError:
            write_bad_log(line, SyntaxError)
        except ValueError:
            write_bad_log(line, ValueError)
        else:
            with open('registrations_good.log', 'a', encoding='utf-8') as good:
                good.write(line)

# TODO, Предлагаю немного оптимизировать наш код. =) Пожалуйста, реализуйте функцию, которая будет:
#  1. принимать на вход строку
#  2. проверять строку.
#  3. вызывать соответствующие исключения, в зависимости от результата проверки строки ()
#  Внутри этой функции ловить исключения не нужно, только вызывать.
#  Саму функцию, стоит запуска внутри основного цикла программы, внутри блоков try/except,
#  чтобы ловить исключения, которые она вызывает =)


# TODO, предлагаю добавить вывод текста ошибки при вызове ошибки
#  Пример:
#  вызов Ошибка("Текст ошибки")
#  В таком случае, сможем ловить ошибки группой в одном блоке except =)

# TODO, ошибки группой можно ловить в одном блоке except следующим образом
#  except (Ошибка1, Ошибка2) as err,
#  Это позволит уйти от большого количества блоков except.
#  при этом, err будет содержать в себе "Текст ошибки" с которым ошибка была вызвана.
#  Что удобно, для записи в файл =)


# TODO, если открывать файлы до основного цикла программы, то наш код отработает быстрее. =)