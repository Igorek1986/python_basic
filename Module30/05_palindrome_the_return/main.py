from collections import Counter

if __name__ == '__main__':
    def can_be_poly(string: str) -> bool:
        counts_alpha = Counter([x for x in string])

        number_of_odd = sum(1 for letter, cnt in counts_alpha.items() if cnt % 2)
        return number_of_odd <= 1


    print(can_be_poly("ababc"))
    print(can_be_poly("abbbc"))

# зачёт!
