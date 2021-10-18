famaly = {('Сидоров', 'Никита'): 35,
          ('Сидорова', 'Алина'): 34,
          ('Сидоров', 'Павел'): 10,
          ('Петров', 'Олег'): 100}

surname = 'Сидорова'.title()


for people, age in famaly.items():
    if surname in people or surname[:-1] in people:
        print(people[0], people[1], age)
