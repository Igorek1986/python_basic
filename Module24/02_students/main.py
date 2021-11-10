from faker import Faker

fake = Faker('ru_RU')

for i in range(10):
    print(fake.name())
