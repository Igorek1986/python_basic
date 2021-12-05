from num_seq import NumberSeq
from collections.abc import Iterable


def num_seq(number: int) -> Iterable[int]:
    count = 0
    if count > number:
        raise StopIteration
    yield count
    count += 1 ** 2


num = int(input('Введите число: '))
print(f'\nКласс-итератор.\nКвадраты чисел до {num}: ', end='')
num_seq_1 = NumberSeq(number=num)

for i_num in num_seq_1:
    print(i_num, end=', ')
print()


print(f'\nФункция-генератор.\nКвадраты чисел до {num}: ', end='')
num_seq_2 = NumberSeq(number=num)
for i_num in num_seq_2:
    print(i_num, end=', ')
print()


print(f'\nГенераторное выражение.\nКвадраты чисел до {num}: ', end='')
num_seq_3 = (i_number ** 2 for i_number in range(1, num + 1))
for i_num in num_seq_3:
    print(i_num, end=', ')
print()
