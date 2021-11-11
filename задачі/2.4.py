a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
res = 1
for i in range(a, b):
    if i % 2 != 0:
        res = res * i
print(res)


