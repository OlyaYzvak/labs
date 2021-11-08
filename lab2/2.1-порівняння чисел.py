num1=input("Enter 3 numbers\n")
num2=input()
num3=input()
min = num1
if num2 < min:
    min = num2
if num3 < min:
    min = num3
print("min num: ", min)
max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3
print("max num:",max)