from num_seq import NumberSeq
from collections.abc import Iterable

# TODO, функция num_seq и модуль num_seq имеют одинаковые названия.
#  Возможно, стоит назвать их по разному.
def num_seq(number: int) -> Iterable[int]:
    count = 0
    # TODO, для реализации функции генератора, вызывать StopIteration не нужно.
    #  Стоит реализовать цикл for с возвратом данных из функции при помощи yield.
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
# TODO, в этом месте кода стоит реализовать цикл по функции num_seq.
num_seq_2 = NumberSeq(number=num)
for i_num in num_seq_2:
    print(i_num, end=', ')
print()


print(f'\nГенераторное выражение.\nКвадраты чисел до {num}: ', end='')
num_seq_3 = (i_number ** 2 for i_number in range(1, num + 1))
for i_num in num_seq_3:
    print(i_num, end=', ')
print()
