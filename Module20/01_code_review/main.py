students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)


def interests_len(my_dict):
    interests = []
    len_surname = 0
    for _, i_data in my_dict.items():
        interests += (i_data['interests'])
        len_surname += len(i_data['surname'])
    return interests, len_surname


for i_id, i_age in students.items():
    print(f"ID студента: {i_id} - возраст: {i_age['age']}")


data_stud = interests_len(students)
print('Полный список интересов всех студентов:\n', data_stud[0])
print('Общая длинна фамилий студентов:', data_stud[1])
