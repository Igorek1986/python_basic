from person import Manager, Agent, Worker

manager_1 = Manager(name='Pavel', surname='Putin', age=23)
manager_2 = Manager(name='Artem', surname='Kovalev', age=2)
manager_3 = Manager(name='Oleg', surname='Ivanov', age=22)
agent_1 = Agent(name='Larisa', surname='Pupkina', age=30)
agent_2 = Agent(name='Marina', surname='Ivanova', age=31)
agent_3 = Agent(name='Olga', surname='Frolova', age=18)
worker_1 = Worker(name='Fedor', surname='Malkin', age=45)
worker_2 = Worker(name='Nikolay', surname='Rasputin', age=43)
worker_3 = Worker(name='Vladimir', surname='Petrov', age=50)

manager_1.payroll(), manager_2.payroll(), manager_3.payroll()
agent_1.payroll(), agent_2.payroll(), agent_3.payroll()
worker_1.payroll(), worker_2.payroll(), worker_3.payroll()

print(f'Зарплата менеджера {manager_1.name} - {manager_1.salary}\n'
      f'Зарплата менеджера {manager_2.name} - {manager_2.salary}\n'
      f'Зарплата менеджера {manager_3.name} - {manager_3.salary}')

print(f'Зарплата менеджера {agent_1.name} - {agent_1.salary}\n'
      f'Зарплата менеджера {agent_2.name} - {agent_2.salary}\n'
      f'Зарплата менеджера {agent_3.name} - {agent_3.salary}')

print(f'Зарплата менеджера {worker_1.name} - {worker_1.salary}\n'
      f'Зарплата менеджера {worker_2.name} - {worker_2.salary}\n'
      f'Зарплата менеджера {worker_3.name} - {worker_3.salary}')

# зачёт!
