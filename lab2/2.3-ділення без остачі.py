number = int(input("Введіть число: "))
range = range(1, number)
for x in range:
    if number % x == 0:
        print(x)



