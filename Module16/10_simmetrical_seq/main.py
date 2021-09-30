def reverse(num_list):
    index = len(num_list) - 1
    for i in range((len(num_list) - 1) // 2):
        temp = num_list[index]
        num_list[index] = num_list[i]
        num_list[i] = temp
        index -= 1
        return num_list


def ans_print(num_list):
    for i in range(len(num_list)):
        print(num_list[i], end=' ')


count = int(input('Длинна списка: '))
number_list = []
revers_list = []
answer_list = []

for i in range(count):
    number = int(input('Введите число: '))
    number_list.append(number)

revers_list.extend(number_list)
revers_list = reverse(revers_list)

print('\nПоследовательность: ', end='')
ans_print(number_list)

for i in range(len(number_list)):
    for _ in range(len(revers_list)):
        if number_list == revers_list:
            break
        else:
            answer_list.append(number_list[i])
            number_list.remove(number_list[0])
            revers_list.remove(revers_list[-1])

reverse(answer_list)

print('\nНужно приписать чисел:', number_list[0])

print('Сами числа:', end=' ')
ans_print(answer_list)

# зачёт!

# #############
# #Разбор ДЗ
# def is_palindrome(num_list):
#     revers_list = []
#     for i_num in range(len(num_list) -1, -1, -1):
#         revers_list.append(num_list[i_num])
#     if num_list == revers_list
#         return True
#     else:
#         return False
#
# nums = [1, 2, 3, 4, 5]
# new_nums = []
# answer = []
#
# for i_nums in range(0, len(nums)):
#     for j_elem in range(i_nums, len(nums)):
#         new_nums.append(nums[j_elem])
#     if is_palindrome(new_nums):
#         for i_answer in range(0, i_nums):
#             answer.append(nums[i_answer])
#             answer.reverse()
#             break
#     new_nums = []
#
# print('Последовательность: ', nums)
# print('Нужно приписать чисел:', len(answer))
# print('Сами числа:', answer)
#
# #############