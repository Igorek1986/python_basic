import random

team_1 = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
team_2 = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
team_3 = [team_1[i] if team_1[i] > team_2[i]
          else team_2[i]
          for i in range(len(team_1))]

print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', team_3)

# зачёт!
