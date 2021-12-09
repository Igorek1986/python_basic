

class NumberSeq:
    def __init__(self, number: int) -> None:
        self.number = number
        self.count = 0

    def __iter__(self) -> "NumberSeq":
        self.count = 0
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count > self.number:
            raise StopIteration
        self.number_seq = self.count ** 2
        return self.number_seq
