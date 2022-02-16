from typing import List

if __name__ == '__main__':
    isprime_lc: List[int] = [x for x in range(2, 1000) if all(x % y != 0 for y in range(2, x))]

    print(isprime_lc)


    def is_prime(number: int) -> List[int]:
        lst_prime = []
        for num in range(2, number):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    lst_prime.append(num)
        return lst_prime


    lst = is_prime(1000)
    print(lst)

# зачёт!
