from faker import Faker
from university import Student
import random

fake = Faker('ru_RU')
student_data = []

for _ in range(10):
    info_student = Student(fake.name(), 5, [random.randint(3, 5) for _ in range(5)])
    # TODO, пожалуйста, обратите внимание, в список ниже необходимо добавлять студентов, "info_student", а не список их аргументов.
    #  Как в таком случае, изменится функция lambda? =)
    student_data.append([info_student.sn, info_student.group_num, info_student.rating_lst, info_student.mid_rating])

student_data.sort(key=lambda key: key[3])


for info in student_data:
    print(f'ФИО: {info[0]} - средний бал: {info[3]}')
