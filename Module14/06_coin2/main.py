def coin(x, y, z):
  if 0 <= x <= z and 0 <= y <= z:
    print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')

x = float(input('Введите координату икс: '))
y = float(input('Введите координату игрек: '))
rad = int(input('Введите радиус:', ))


coin(x, y, rad)