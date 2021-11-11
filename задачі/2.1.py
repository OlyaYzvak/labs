a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
numbers = [a, b, c]
res = 0
for i in numbers:
    if i >= 0:
        res = res + 1
print("додатніх чисел: ", res)
