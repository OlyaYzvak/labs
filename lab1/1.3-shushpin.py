a = int(input())
b = int(input())
c = int(input())
d = int(input())
res = (a // 3) + (b // 3) + (c // 3) + (d // 3)
if (a%3 > 0): res = res + 1
if (b%3 > 0): res = res + 1
if (c%3 > 0): res = res + 1
if (d%3 > 0): res = res + 1

print('res = ', res)
