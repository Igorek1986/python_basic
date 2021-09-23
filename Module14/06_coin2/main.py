def coin(x, y):
  if 0 <= x <= rad and 0 <= y <= rad:
    print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')

x = float(input('Введите координату икс: '))
y = float(input('Введите координату игрек: '))
rad = int(input('Введите радиус:', ))
coin(x, y)