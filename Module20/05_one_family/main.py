famaly = {('Сидоров', 'Никита'): 35,
          ('Сидорова', 'Алина'): 34,
          ('Сидоров', 'Павел'): 10,
          ('Петров', 'Олег'): 100}

surname = input('ведите фамилию: ').title()
if surname[-1] == 'а':
    surname = surname[:-1]

for people, age in famaly.items():
    if surname in people[0]:
        print(people[0], people[1], age)

# зачёт!
