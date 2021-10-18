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


lst_elements = []
i_is_prime(object_elements)
print(lst_elements)
