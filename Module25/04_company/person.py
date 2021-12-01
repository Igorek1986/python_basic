class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Employee(Person):
    def __init__(self, name, surname, age, salary=0):
        super().__init__(name, surname, age)
        self.salary = salary

    def payroll(self):
        self.salary = 0


class Manager(Employee):

    def payroll(self):
        self.salary = 13000


class Agent(Employee):
    volume_of_sales = 100000

    def payroll(self):
        self.salary = 5000 + self.volume_of_sales * 5 / 100


class Worker(Employee):
    time_work = 176

    def payroll(self):
        self.salary = 100 * self.time_work
