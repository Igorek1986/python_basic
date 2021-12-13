from collections.abc import Iterable


class Qsequence:
    def __init__(self, lst: list):
        if not lst[0] == 1 or not lst[1] == 1:
            raise StopIteration()
        self.lst = lst[:]

    def __next__(self):
        q_cur = self.lst[-self.lst[-1]] + self.lst[-self.lst[-2]]
        self.lst.append(q_cur)
        return q_cur

    def __iter__(self) -> Iterable[int]:
        return self


def hof_seq(lst: list, n: int) -> Iterable[int]:
    lst = lst[:]
    if not lst[0] == 1 or not lst[1] == 1:
        # для выхода из функции генератора стоит использовать return.
        raise StopIteration()
    else:
        for num in range(n):
            q_cur = lst[-lst[-1]] + lst[-lst[-2]]
            lst.append(q_cur)
            yield q_cur


num_search = int(input('Сколько чисел ищем в последовательности? '))
print('Итератор: ', end='')
q_num = Qsequence([1, 1])
for _ in range(num_search):
    print(next(q_num), end='')

print('\nГенератор: ', end='')
q_num_1 = hof_seq(lst=[1, 1], n=num_search)
for i_num in q_num_1:
    print(i_num, end='')

# зачёт!
