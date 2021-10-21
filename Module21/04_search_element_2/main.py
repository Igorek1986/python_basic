def find_key(structure, key, depth=2):
	if key in structure and depth != 0:
		return structure[key]

	for sub_structure in structure.values():
		if isinstance(sub_structure, dict):
			if depth == 0:
				return None

			result = find_key(sub_structure, key, depth=depth)
			depth -= 1
			if result:
				break
	else:
		result = None
	return result


site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


key_user = input('Какой ключ ищем? ')
while True:
	question = input('Установить глубину поиска? ').title()
	if question == 'Yes':
		depth_user = int(input('Введите глубину: '))
		break
	elif question == 'No':
		depth_user = 2
		break
	else:
		print('Ошибка ввода! Введите "Yes" или "No"')


find_result = find_key(site, key_user, depth=depth_user)
if find_result:
	print(find_result)
else:
	print('Такого ключа нет в структуре сайта на данной глубине ')

# Какой ключ ищем? h2
# Установить глубину поиска? Yes
# Введите глубину: 2
# Здесь будет мой заголовок
# TODO, пожалуйста, обратите внимание, ключ h2 есть на 3ем уровне, на 2ом, мы найти его не должны. =)