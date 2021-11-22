from faker import Faker
from university import Student
import random

fake = Faker('ru_RU')
student_data = []

for _ in range(10):
    info_student = Student(fake.name(), 5, [random.randint(3, 5) for _ in range(5)])
    student_data.append(info_student)

student_data.sort(key=lambda key: key.mid_rating)

for info in student_data:
    print(f'ФИО: {info.sn} - средний бал: {info.mid_rating}')

# зачёт!
