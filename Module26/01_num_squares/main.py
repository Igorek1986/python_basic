from num_seq import NumberSeq
from collections.abc import Iterable


def square_number(number: int) -> Iterable[int]:
    for i_num in range(1, number + 1):
        yield i_num ** 2


num = int(input('Введите число: '))
print(f'\nКласс-итератор.\nКвадраты чисел до {num}: ', end='')
num_seq_1 = NumberSeq(number=num)

for i_num in num_seq_1:
    print(i_num, end=', ')
print()


print(f'\nФункция-генератор.\nКвадраты чисел до {num}: ', end='')
num_seq_2 = square_number(number=num)
for i_num in num_seq_2:
    print(i_num, end=', ')
print()


print(f'\nГенераторное выражение.\nКвадраты чисел до {num}: ', end='')
num_seq_3 = (i_number ** 2 for i_number in range(1, num + 1))
for i_num in num_seq_3:
    print(i_num, end=', ')
print()
