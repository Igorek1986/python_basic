class Person:
    def __init__(self, name, surname, age):
        self.__set_name(name)
        self.__set_surname(surname)
        self.__set_age(age)

    def __set_name(self, name):
        self.__name = name

    def __set_surname(self, surname):
        self.__surname = surname

    def __set_age(self, age):
        self.__age = age


class Employee(Person):
    def __init__(self, name, surname, age, salary=0):
        super().__init__(name, surname, age)
        # self.set_salary(salary)
        # self.volume_of_sales = 0

    def payroll(self):
        self.salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return


class Manager(Employee):

    def payroll(self):
        self.salary = 13000


class Agent(Employee):
    pass


class Worker(Employee):
    # volume_of_sales
    pass


manager = Manager(name='Pavel', surname='Putin', age=23)
manager.payroll()
print(manager.salary)
