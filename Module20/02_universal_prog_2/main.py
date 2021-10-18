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
    if isinstance(data, dict):
        elem = dict(data.items())
    else:
        elem = data
    return [value for index, value in enumerate(elem) if is_prime(index)]


# object_elements = (0, 1, 2, 3, 4, 5)
# object_elements = ('0123456789')
# object_elements = [0, 1, 2, 3, 4, 5]
object_elements = {1: 'n', 2: 2, 3: 3, 4: 4, 5: 5, 17: 7}


print(i_is_prime(object_elements))
