a = int(input("Введіть число 1: "))
b = int(input("Введіть число 2: "))
c = int(input("Введіть число 3: "))
d = int(input("Введіть число 4: "))
numbers = [a, b, c, d]
print("Парні:")
for x in numbers:
    if x % 2 == 0:
        print(x)
print("Непарні:")
for x in numbers:
    if x % 2 != 0:
        print(x)

