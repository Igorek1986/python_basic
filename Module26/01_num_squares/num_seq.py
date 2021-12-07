from collections.abc import Iterable


class NumberSeq:
    def __init__(self, number: int) -> None:
        self.number = number
        self.count = 0

    # TODO, т.к. в этом методе класс возвращает сам себя, то стоит указать возврат "NumberSeq" вместо Iterable[int]
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count > self.number:
            raise StopIteration
        self.number_seq = self.count ** 2
        return self.number_seq
