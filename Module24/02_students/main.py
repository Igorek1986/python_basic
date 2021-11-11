from faker import Faker
from university import Student
import random

fake = Faker('ru_RU')
new_lst = []

for _ in range(10):
    i = Student(fake.name(), 5, [random.randint(3, 5) for _ in range(5)])

    # TODO, пожалуйста, обратите внимание, в списке стоит хранить объекты классов Студент.
    #  Как в таком случае изменится функция lambda при сортировке? =)
    new_lst.append([i.sn, i.mid_rating])

new_lst.sort(key=lambda key: key[1])


for info in new_lst:
    print(f'ФИО: {info[0]} - средний бал: {info[1]}')
