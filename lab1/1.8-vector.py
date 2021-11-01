import math

ax = int(input('Введіть координату x точки a: '))
ay = int(input('Введіть координату у точки а: '))
bx = int(input('Введіть координату x точки b: '))
by = int(input('Введіть координату у точки b: '))

res = math.sqrt(math.pow(bx - ax, 2) + math.pow(by - ay, 2))
print('Відстань між точками: ', res)


