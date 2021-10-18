def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    for i_num in range(2, number):
        if number % i_num == 0:
            return False
    return True


def i_is_prime(data):
    # TODO
    #  1. Предлагаю попробовать решить задание в одну строку кода при помощи List comprehensions.
    #  2. С enumerate в цикле правильно так "for index, value in enumerate(object):"
    #  Это решение позволит сократить количество вычислений по индексам. =)
    #  3. Предлагаю сократить количество повторяющегося кода.
    #  К примеру, вынести цикл за пределы условного оператора, а в условном операторе определять только переменную,
    #  по которой пойдём в цикле.
    if not isinstance(data, dict):
        for i in enumerate(data):
            if is_prime(i[0]):
                lst_elements.append(i[1])
    else:
        for i in data.items():
            if is_prime(i[0]):
                lst_elements.append(i[1])


# object_elements = (0, 1, 2, 3, 4, 5)
# object_elements = ('0123456789')
# object_elements = [0, 1, 2, 3, 4, 5]
object_elements = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 17: 7}


lst_elements = []  # TODO, список получился лишним. =)
i_is_prime(object_elements)
print(lst_elements)
