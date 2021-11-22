class Student:

    def __init__(self, sn, group_num, rating_lst=[]):
        self.sn = sn
        self.group_num = group_num
        self.rating_lst = rating_lst
        self.mid_rating = sum(rating_lst) / len(rating_lst)

    def print_info(self):
        print(f'ФИО: {self.sn}\nНомер группы {self.group_num}\nОценки: {self.rating_lst}\n'
              f'Средний рейтинг: {self.mid_rating}')

    def __lt__(self, other):
        return self.mid_rating < other.mid_rating
